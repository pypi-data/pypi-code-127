"""
Main driver class for PypeIt run

.. include common links, assuming primary doc root is up one directory
.. include:: ../include/links.rst

"""
import time
import os
import copy
import json

from IPython import embed

import numpy as np

from configobj import ConfigObj

from astropy.io import fits
from astropy.table import Table

from pypeit import inputfiles
from pypeit.core import parse
from pypeit import masterframe
from pypeit import msgs
from pypeit import calibrations
from pypeit.images import buildimage
from pypeit.display import display
from pypeit import find_objects
from pypeit import extraction
from pypeit import spec2dobj
from pypeit.core import qa
from pypeit.core import findobj_skymask
from pypeit import specobjs
from pypeit.spectrographs.util import load_spectrograph
from pypeit import slittrace
from pypeit import utils
from pypeit.history import History
from pypeit.par import PypeItPar
from pypeit.metadata import PypeItMetaData
from pypeit.manual_extract import ManualExtractionObj

from linetools import utils as ltu

class PypeIt:
    """
    This class runs the primary calibration and extraction in PypeIt

    .. todo::
        Fill in list of attributes!

    Args:
        pypeit_file (:obj:`str`):
            PypeIt filename.
        verbosity (:obj:`int`, optional):
            Verbosity level of system output.  Can be:

                - 0: No output
                - 1: Minimal output (default)
                - 2: All output

        overwrite (:obj:`bool`, optional):
            Flag to overwrite any existing files/directories.
        reuse_masters (:obj:`bool`, optional):
            Reuse any pre-existing calibration files
        logname (:obj:`str`, optional):
            The name of an ascii log file with the details of the
            reduction.
        show: (:obj:`bool`, optional):
            Show reduction steps via plots (which will block further
            execution until clicked on) and outputs to ginga. Requires
            remote control ginga session via ``ginga --modules=RC,SlitWavelength &``
        redux_path (:obj:`str`, optional):
            Over-ride reduction path in PypeIt file (e.g. Notebook usage)
        calib_only: (:obj:`bool`, optional):
            Only generate the calibration files that you can

    Attributes:
        pypeit_file (:obj:`str`):
            Name of the pypeit file to read.  PypeIt files have a
            specific set of valid formats. A description can be found
            :ref:`pypeit_file`.
        fitstbl (:obj:`pypeit.metadata.PypeItMetaData`): holds the meta info

    """
    def __init__(self, pypeit_file, verbosity=2, overwrite=True, reuse_masters=False, logname=None,
                 show=False, redux_path=None, calib_only=False):

        # Set up logging
        self.logname = logname
        self.verbosity = verbosity
        self.pypeit_file = pypeit_file
        
        self.msgs_reset()
        
        # Load up PypeIt file
        self.pypeItFile = inputfiles.PypeItFile.from_file(pypeit_file)
        self.calib_only = calib_only

        # Spectrograph
        spectrograph_name = self.pypeItFile.config['rdx']['spectrograph']
        self.spectrograph = load_spectrograph(spectrograph_name)
        msgs.info('Loaded spectrograph {0}'.format(self.spectrograph.name))

        # --------------------------------------------------------------
        # Get the full set of PypeIt parameters
        #   - Grab a science or standard file for configuration specific parameters

        config_specific_file = None
        for idx, row in enumerate(self.pypeItFile.data):
            if ('science' in row['frametype']) or ('standard' in row['frametype']):
                config_specific_file = self.pypeItFile.filenames[idx]
        # search for arcs, trace if no scistd was there
        if config_specific_file is None:
            for idx, row in enumerate(self.pypeItFile.data):
                if ('arc' in row['frametype']) or ('trace' in row['frametype']):
                    config_specific_file = self.pypeItFile.filenames[idx]
        if config_specific_file is not None:
            msgs.info(
                'Setting configuration-specific parameters using {0}'.format(os.path.split(config_specific_file)[1]))
        spectrograph_cfg_lines = self.spectrograph.config_specific_par(config_specific_file).to_config()

        #   - Build the full set, merging with any user-provided
        #     parameters
        self.par = PypeItPar.from_cfg_lines(cfg_lines=spectrograph_cfg_lines, 
                                            merge_with=self.pypeItFile.cfg_lines)
        msgs.info('Built full PypeIt parameter set.')

        # Check the output paths are ready
        if redux_path is not None:
            self.par['rdx']['redux_path'] = redux_path

        # TODO: Write the full parameter set here?
        # --------------------------------------------------------------

        # --------------------------------------------------------------
        # Build the meta data
        #   - Re-initilize based on the file data
        msgs.info('Compiling metadata')
        self.fitstbl = PypeItMetaData(self.spectrograph, self.par, 
                                      files=self.pypeItFile.filenames,
                                      usrdata=self.pypeItFile.data, 
                                      strict=True)
        #   - Interpret automated or user-provided data from the PypeIt
        #   file
        self.fitstbl.finalize_usr_build(
            self.pypeItFile.frametypes, 
            self.pypeItFile.setup_name)

        
        # --------------------------------------------------------------
        #   - Write .calib file (For QA naming amongst other things)
        calib_file = pypeit_file.replace('.pypeit', '.calib')
        self.fitstbl.write_calib(calib_file)

        # Other Internals
        self.overwrite = overwrite

        # Currently the runtime argument determines the behavior for
        # reuse_masters.
        self.reuse_masters = reuse_masters
        self.show = show

        # Set paths
        self.calibrations_path = os.path.join(self.par['rdx']['redux_path'], self.par['calibrations']['master_dir'])

        # Check for calibrations
        if not self.calib_only:
            calibrations.check_for_calibs(self.par, self.fitstbl,
                                          raise_error=self.par['calibrations']['raise_chk_error'])

        # Report paths
        msgs.info('Setting reduction path to {0}'.format(self.par['rdx']['redux_path']))
        msgs.info('Master calibration data output to: {0}'.format(self.calibrations_path))
        msgs.info('Science data output to: {0}'.format(self.science_path))
        msgs.info('Quality assessment plots output to: {0}'.format(self.qa_path))
        # TODO: Is anything written to the qa dir or only to qa/PNGs?
        # Should we have separate calibration and science QA
        # directories?
        # An html file wrapping them all too

        # Init
        # TODO: I don't think this ever used

        self.det = None

        self.tstart = None
        self.basename = None
        self.sciI = None
        self.obstime = None

    @property
    def science_path(self):
        """Return the path to the science directory."""
        return os.path.join(self.par['rdx']['redux_path'], self.par['rdx']['scidir'])

    @property
    def qa_path(self):
        """Return the path to the top-level QA directory."""
        return os.path.join(self.par['rdx']['redux_path'], self.par['rdx']['qadir'])

    def build_qa(self):
        """
        Generate QA wrappers
        """
        msgs.qa_path = self.qa_path
        qa.gen_qa_dir(self.qa_path)
        qa.gen_mf_html(self.pypeit_file, self.qa_path)
        qa.gen_exp_html()

    # TODO: This should go in a more relevant place
    def spec_output_file(self, frame, twod=False):
        """
        Return the path to the spectral output data file.
        
        Args:
            frame (:obj:`int`):
                Frame index from :attr:`fitstbl`.
            twod (:obj:`bool`):
                Name for the 2D output file; 1D file otherwise.
        
        Returns:
            :obj:`str`: The path for the output file
        """
        return os.path.join(self.science_path, 'spec{0}d_{1}.fits'.format('2' if twod else '1',
                                                    self.fitstbl.construct_basename(frame)))

    def outfile_exists(self, frame):
        """
        Check whether the 2D outfile of a given frame already exists

        Args:
            frame (int): Frame index from fitstbl

        Returns:
            bool: True if the 2d file exists, False if it does not exist
        """
        return os.path.isfile(self.spec_output_file(frame, twod=True))

    def get_std_outfile(self, standard_frames):
        """
        Grab the output filename from an input list of standard_frame indices

        If more than one index is provided, the first is taken

        Args:
            standard_frames (list): List of indices corresponding to standard stars

        Returns:
            str: Full path to the standard spec1d output file
        """
        # TODO: Need to decide how to associate standards with
        # science frames in the case where there is more than one
        # standard associated with a given science frame.  Below, I
        # just use the first standard

        std_outfile = None
        std_frame = None if len(standard_frames) == 0 else standard_frames[0]
        # Prepare to load up standard?
        if std_frame is not None:
            std_outfile = self.spec_output_file(std_frame) \
                            if isinstance(std_frame, (int,np.integer)) else None
        if std_outfile is not None and not os.path.isfile(std_outfile):
            msgs.error('Could not find standard file: {0}'.format(std_outfile))
        return std_outfile

    def calib_all(self, run=True):
        """
        Create calibrations for all setups

        This will not crash if not all of the standard set of files are not provided

        Args:
            run (bool, optional): If False, only print the calib names and do
            not actually run.  Only used with the pypeit_parse_calib_id script

        Returns:
            dict: A simple dict summarizing the calibration names
        """
        calib_dict = {}

        self.tstart = time.time()

        # Frame indices
        frame_indx = np.arange(len(self.fitstbl))
        for i in range(self.fitstbl.n_calib_groups):
            # 1-indexed calib number
            calib_grp = str(i+1)
            # Find all the frames in this calibration group
            in_grp = self.fitstbl.find_calib_group(i)
            grp_frames = frame_indx[in_grp]

            # Find the detectors to reduce
#            detectors = PypeIt.select_detectors(detnum=self.par['rdx']['detnum'],
#                                                ndet=self.spectrograph.ndet)
            subset = self.par['rdx']['slitspatnum'] if self.par['rdx']['slitspatnum'] is not None \
                else self.par['rdx']['detnum']
            detectors = self.spectrograph.select_detectors(subset=subset)
            msgs.info(f'Detectors to work on: {detectors}')

            calib_dict[calib_grp] = {}

            # Loop on Detectors
            for self.det in detectors:
                msgs.info("Working on detector {0}".format(self.det))
                # Instantiate Calibrations class
                self.caliBrate = calibrations.Calibrations.get_instance(
                    self.fitstbl, self.par['calibrations'], self.spectrograph,
                    self.calibrations_path, qadir=self.qa_path, reuse_masters=self.reuse_masters,
                    show=self.show,
                    user_slits=slittrace.merge_user_slit(self.par['rdx']['slitspatnum'],
                                                         self.par['rdx']['maskIDs']))
                # Do it
                # TODO: Why isn't set_config part of the Calibrations.__init__ method?
                self.caliBrate.set_config(grp_frames[0], self.det, self.par['calibrations'])

                # Allow skipping the run (e.g. parse_calib_id.py script)
                if run:
                    self.caliBrate.run_the_steps()
                    if not self.caliBrate.success:
                        msgs.warn(f'Calibrations for detector {self.det} were unsuccessful!  The step '
                                  f'that failed was {self.caliBrate.failed_step}.  Continuing by '
                                  f'skipping this detector.')

                key = self.caliBrate.master_key_dict['frame']
                calib_dict[calib_grp][key] = {}
                for step in self.caliBrate.steps:
                    if step in ['bpm', 'slits', 
                                'wv_calib', 'tilts', 'flats']:
                        continue
                    elif step == 'tiltimg':  # Annoying kludge
                        step = 'tilt'
                    # Prep
                    raw_files, self.caliBrate.master_key_dict[step] = self.caliBrate._prep_calibrations(step)
                    masterframe_name = masterframe.construct_file_name(
                        buildimage.frame_image_classes[step],
                        self.caliBrate.master_key_dict[step], 
                        master_dir=self.caliBrate.master_dir)

                    # Add to dict
                    if len(raw_files) > 0:
                        calib_dict[calib_grp][key][step] = {}
                        calib_dict[calib_grp][key][step]['master_key'] = self.caliBrate.master_key_dict[step]
                        calib_dict[calib_grp][key][step]['master_name'] = os.path.basename(masterframe_name)
                        calib_dict[calib_grp][key][step]['raw_files'] = [os.path.basename(ifile) for ifile in raw_files]

        # Print the results
        print(json.dumps(calib_dict, sort_keys=True, indent=4))

        # Write
        msgs.info('Writing calib file')
        calib_file = self.pypeit_file.replace('.pypeit', '.calib_ids')
        ltu.savejson(calib_file, calib_dict, overwrite=True, easy_to_read=True)

        # Finish
        self.print_end_time()

        # Return
        return calib_dict

    def reduce_all(self):
        """
        Main driver of the entire reduction

        Calibration and extraction via a series of calls to reduce_exposure()

        """
        # Validate the parameter set
        self.par.validate_keys(required=['rdx', 'calibrations', 'scienceframe', 'reduce',
                                         'flexure'])
        self.tstart = time.time()

        # Find the standard frames
        is_standard = self.fitstbl.find_frames('standard')

        # Find the science frames
        is_science = self.fitstbl.find_frames('science')
        # this will give an error to alert the user that no reduction
        # will be run if there are no science/standard frames and `run_pypeit` is run without -c flag
        if not np.any(is_science) and not np.any(is_standard):
            msgs.error('No science/standard frames provided. Add them to your PypeIt file '
                       'if this is a standard run! Otherwise run calib_only reduction using -c flag')

        # Frame indices
        frame_indx = np.arange(len(self.fitstbl))

        # Standard Star(s) Loop
        # Iterate over each calibration group and reduce the standards
        for i in range(self.fitstbl.n_calib_groups):

            # Find all the frames in this calibration group
            in_grp = self.fitstbl.find_calib_group(i)

            # Find the indices of the standard frames in this calibration group:
            grp_standards = frame_indx[is_standard & in_grp]

            # Reduce all the standard frames, loop on unique comb_id
            u_combid_std= np.unique(self.fitstbl['comb_id'][grp_standards])
            for j, comb_id in enumerate(u_combid_std):
                frames = np.where(self.fitstbl['comb_id'] == comb_id)[0]
                bg_frames = np.where(self.fitstbl['bkg_id'] == comb_id)[0]
                if not self.outfile_exists(frames[0]) or self.overwrite:
                    # Build history to document what contributd to the reduced
                    # exposure
                    history = History(self.fitstbl.frame_paths(frames[0]))
                    history.add_reduce(i, self.fitstbl, frames, bg_frames)
                    std_spec2d, std_sobjs = self.reduce_exposure(frames, bg_frames=bg_frames)

                    # TODO come up with sensible naming convention for save_exposure for combined files
                    self.save_exposure(frames[0], std_spec2d, std_sobjs, self.basename, history)
                else:
                    msgs.info('Output file: {:s} already exists'.format(self.fitstbl.construct_basename(frames[0])) +
                              '. Set overwrite=True to recreate and overwrite.')

        # Science Frame(s) Loop
        # Iterate over each calibration group again and reduce the science frames
        for i in range(self.fitstbl.n_calib_groups):
            # Find all the frames in this calibration group
            in_grp = self.fitstbl.find_calib_group(i)

            # Find the indices of the science frames in this calibration group:
            grp_science = frame_indx[is_science & in_grp]
            # Associate standards (previously reduced above) for this setup
            std_outfile = self.get_std_outfile(frame_indx[is_standard])
            # Reduce all the science frames; keep the basenames of the science frames for use in flux calibration
            science_basename = [None]*len(grp_science)
            # Loop on unique comb_id
            u_combid = np.unique(self.fitstbl['comb_id'][grp_science])
        
            for j, comb_id in enumerate(u_combid):
                frames = np.where(self.fitstbl['comb_id'] == comb_id)[0]
                # Find all frames whose comb_id matches the current frames bkg_id.
                bg_frames = np.where((self.fitstbl['comb_id'] == self.fitstbl['bkg_id'][frames][0]) &
                                     (self.fitstbl['comb_id'] >= 0))[0]
                # JFH changed the syntax below to that above, which allows frames to be used more than once
                # as a background image. The syntax below would require that we could somehow list multiple
                # numbers for the bkg_id which is impossible without a comma separated list
#                bg_frames = np.where(self.fitstbl['bkg_id'] == comb_id)[0]
                if not self.outfile_exists(frames[0]) or self.overwrite:

                    # Build history to document what contributd to the reduced
                    # exposure
                    history = History(self.fitstbl.frame_paths(frames[0]))
                    history.add_reduce(i, self.fitstbl, frames, bg_frames)

                    # TODO -- Should we reset/regenerate self.slits.mask for a new exposure
                    sci_spec2d, sci_sobjs = self.reduce_exposure(frames, bg_frames=bg_frames,
                                                    std_outfile=std_outfile)
                    science_basename[j] = self.basename

                    # TODO come up with sensible naming convention for save_exposure for combined files
                    if len(sci_spec2d.detectors) > 0:
                        self.save_exposure(frames[0], sci_spec2d, sci_sobjs, self.basename, history)
                    else:
                        msgs.warn('No spec2d and spec1d saved to file because the '
                                  'calibration/reduction was not successful for all the detectors')
                else:
                    msgs.warn('Output file: {:s} already exists'.format(self.fitstbl.construct_basename(frames[0])) +
                              '. Set overwrite=True to recreate and overwrite.')

            msgs.info('Finished calibration group {0}'.format(i))

        # Finish
        self.print_end_time()

    def reduce_exposure(self, frames, bg_frames=None, std_outfile=None):
        """
        Reduce a single exposure

        Args:
            frames (:obj:`list`):
                List of 0-indexed rows in :attr:`fitstbl` with the frames to
                reduce.
            bg_frames (:obj:`list`, optional):
                List of frame indices for the background.
            std_outfile (:obj:`str`, optional):
                File with a previously reduced standard spectrum from
                PypeIt.

        Returns:
            dict: The dictionary containing the primary outputs of
            extraction.

        """

        # if show is set, clear the ginga channels at the start of each new sci_ID
        if self.show:
            # TODO: Put this in a try/except block?
            display.clear_all(allow_new=True)

        has_bg = True if bg_frames is not None and len(bg_frames) > 0 else False
        # Is this an b/g subtraction reduction?
        if has_bg:
            self.bkg_redux = True
            # The default is to find_negative objects if the bg_frames are classified as "science", and to not find_negative
            # objects if the bg_frames are classified as "sky". This can be explicitly overridden if
            # par['reduce']['findobj']['find_negative'] is set to something other than the default of None.
            self.find_negative = (('science' in self.fitstbl['frametype'][bg_frames[0]]) |
                                  ('standard' in self.fitstbl['frametype'][bg_frames[0]]))\
                if self.par['reduce']['findobj']['find_negative'] is None else self.par['reduce']['findobj']['find_negative']
        else:
            self.bkg_redux = False
            self.find_negative= False

        # Container for all the Spec2DObj
        all_spec2d = spec2dobj.AllSpec2DObj()
        all_spec2d['meta']['bkg_redux'] = self.bkg_redux
        all_spec2d['meta']['find_negative'] = self.find_negative
        # TODO -- Should we reset/regenerate self.slits.mask for a new exposure

        # container for specobjs during first loop (objfind)
        all_specobjs_objfind = specobjs.SpecObjs()
        # container for specobjs during second loop (extraction)
        all_specobjs_extract = specobjs.SpecObjs()
        # list of global_sky obtained during objfind and used in extraction
        initial_sky_list = []
        # list of sciImg
        sciImg_list = []
        # List of detectors with successful calibration
        calibrated_det = []
        # list of successful MasterSlits calibrations to be used in the extraction loop
        calib_slits = []
        # List of objFind objects
        objFind_list = []


        # Print status message
        msgs_string = 'Reducing target {:s}'.format(self.fitstbl['target'][frames[0]]) + msgs.newline()
        # TODO: Print these when the frames are actually combined,
        # backgrounds are used, etc?
        msgs_string += 'Combining frames:' + msgs.newline()
        for iframe in frames:
            msgs_string += '{0:s}'.format(self.fitstbl['filename'][iframe]) + msgs.newline()
        msgs.info(msgs_string)
        if has_bg:
            bg_msgs_string = ''
            for iframe in bg_frames:
                bg_msgs_string += '{0:s}'.format(self.fitstbl['filename'][iframe]) + msgs.newline()
            bg_msgs_string = msgs.newline() + 'Using background from frames:' + msgs.newline() + bg_msgs_string
            msgs.info(bg_msgs_string)

        # Find the detectors to reduce
        subset = self.par['rdx']['slitspatnum'] if self.par['rdx']['slitspatnum'] is not None \
                    else self.par['rdx']['detnum']
        detectors = self.spectrograph.select_detectors(subset=subset)
        msgs.info(f'Detectors to work on: {detectors}')

        # Loop on Detectors
        # TODO: Attempt to put in a multiprocessing call here?
        # objfind
        for self.det in detectors:
            msgs.info("Working on detector {0}".format(self.det))
            # run calibration
            self.caliBrate = self.calib_one(frames, self.det)
            if not self.caliBrate.success:
                msgs.warn(f'Calibrations for detector {self.det} were unsuccessful!  The step '
                          f'that failed was {self.caliBrate.failed_step}.  Continuing by '
                          f'skipping this detector.')
                continue

            # we save only the detectors that had a successful calibration,
            # and we use only those in the extract loop below
            calibrated_det.append(self.det)
            # we also save the successful MasterSlits calibrations because they are used and modified
            # in the slitmask stuff in between the two loops
            calib_slits.append(self.caliBrate.slits)
            # global_sky, skymask and sciImg are needed in the extract loop
            initial_sky, sobjs_obj, sciImg, objFind = self.objfind_one(frames, self.det, bg_frames,
                                                                       std_outfile=std_outfile)
            if len(sobjs_obj)>0:
                all_specobjs_objfind.add_sobj(sobjs_obj)
            initial_sky_list.append(initial_sky)
            sciImg_list.append(sciImg)
            objFind_list.append(objFind)

        # slitmask stuff
        if len(calibrated_det) > 0 and self.par['reduce']['slitmask']['assign_obj']:
            # get object positions from slitmask design and slitmask offsets for all the detectors
            spat_flexure = np.array([ss.spat_flexure for ss in sciImg_list])
            # Grab platescale with binning
            bin_spec, bin_spat = parse.parse_binning(self.binning)
            platescale = np.array([ss.detector.platescale*bin_spat for ss in sciImg_list])
            # get the dither offset if available
            if self.par['reduce']['slitmask']['use_dither_offset']:
                dither = self.spectrograph.parse_dither_pattern(
                    [self.fitstbl.frame_paths(frames[0])])
                dither_off = dither[2][0] if dither is not None else None
            else:
                dither_off = None
            calib_slits = slittrace.get_maskdef_objpos_offset_alldets(
                all_specobjs_objfind, calib_slits, spat_flexure, platescale,
                self.par['calibrations']['slitedges']['det_buffer'],
                self.par['reduce']['slitmask'], dither_off=dither_off)
            # determine if slitmask offsets exist and compute an average offsets over all the detectors
            calib_slits = slittrace.average_maskdef_offset(
                calib_slits, platescale[0], self.spectrograph.list_detectors(mosaic='MSC' in calib_slits[0].detname))
            # slitmask design matching and add undetected objects
            all_specobjs_objfind = slittrace.assign_addobjs_alldets(
                all_specobjs_objfind, calib_slits, spat_flexure, platescale,
                self.par['reduce']['slitmask'], self.par['reduce']['findobj']['find_fwhm'])

        # Extract
        for i, self.det in enumerate(calibrated_det):
            # re-run (i.e., load) calibrations
            self.caliBrate = self.calib_one(frames, self.det)
            self.caliBrate.slits = calib_slits[i]

            detname = sciImg_list[i].detector.name

            # TODO: pass back the background frame, pass in background
            # files as an argument. extract one takes a file list as an
            # argument and instantiates science within
            if all_specobjs_objfind.nobj > 0:
                all_specobjs_on_det = all_specobjs_objfind[all_specobjs_objfind.DET == detname]
            else:
                all_specobjs_on_det = all_specobjs_objfind

            # Extract
            all_spec2d[detname], tmp_sobjs \
                    = self.extract_one(frames, self.det, sciImg_list[i], objFind_list[i],
                                       initial_sky_list[i], all_specobjs_on_det)
            # Hold em
            if tmp_sobjs.nobj > 0:
                all_specobjs_extract.add_sobj(tmp_sobjs)
            # JFH TODO write out the background frame?

            # TODO -- Save here?  Seems like we should.  Would probably need to use update_det=True

        # Return
        return all_spec2d, all_specobjs_extract

    def get_sci_metadata(self, frame, det):
        """
        Grab the meta data for a given science frame and specific detector

        Args:
            frame (int): Frame index
            det (int): Detector index

        Returns:
            5 objects are returned::
                - str: Object type;  science or standard
                - str: Setup string from master_key()
                - astropy.time.Time: Time of observation
                - str: Basename of the frame
                - str: Binning of the detector

        """

        # Set binning, obstime, basename, and objtype
        binning = self.fitstbl['binning'][frame]
        obstime  = self.fitstbl.construct_obstime(frame)
        basename = self.fitstbl.construct_basename(frame, obstime=obstime)
        objtype  = self.fitstbl['frametype'][frame]
        if 'science' in objtype:
            objtype_out = 'science'
        elif 'standard' in objtype:
            objtype_out = 'standard'
        else:
            msgs.error('Unrecognized objtype')
        setup = self.fitstbl.master_key(frame, det=det)
        return objtype_out, setup, obstime, basename, binning


    def calib_one(self, frames, det):
        """
        Run Calibration for a single exposure/detector pair

        Args:
            frames (:obj:`list`):
                List of frames to extract; stacked if more than one
                is provided
            det (:obj:`int`):
                Detector number (1-indexed)

        Returns:
            caliBrate (:class:`pypeit.calibrations.Calibrations`)

        """

        msgs.info("Working on detector {0}".format(det))
        # Instantiate Calibrations class
        caliBrate = calibrations.Calibrations.get_instance(
            self.fitstbl, self.par['calibrations'], self.spectrograph,
            self.calibrations_path, qadir=self.qa_path, 
            reuse_masters=self.reuse_masters,
            show=self.show, 
            user_slits=slittrace.merge_user_slit(
                self.par['rdx']['slitspatnum'], self.par['rdx']['maskIDs']))
            #slitspat_num=self.par['rdx']['slitspatnum'])
        # These need to be separate to accomodate COADD2D
        caliBrate.set_config(frames[0], det, self.par['calibrations'])
        caliBrate.run_the_steps()

        return caliBrate

    def objfind_one(self, frames, det, bg_frames, std_outfile=None):
        """
        Reduce + Find Objects in a single exposure/detector pair

        sci_ID and det need to have been set internally prior to calling this method

        Parameters
        ----------
        frames : :obj:`list`
            List of frames to extract; stacked if more than one is provided
        det : :obj:`int`
            Detector number (1-indexed)
        bg_frames : :obj:`list`
            List of frames to use as the background. Can be empty.
        std_outfile : :obj:`str`, optional
            Filename for the standard star spec1d file. Passed directly to
            :func:`get_std_trace`.

        Returns
        -------
        global_sky : `numpy.ndarray`_
            Initial global sky model
        sobjs_obj : :class:`~pypeit.specobjs.SpecObjs`
            List of objects found
        sciImg : :class:`~pypeit.images.pypeitimage.PypeItImage`
            Science image
        objFind : :class:`~pypeit.find_objects.FindObjects`
            Object finding speobject

        """
        # Grab some meta-data needed for the reduction from the fitstbl
        self.objtype, self.setup, self.obstime, self.basename, self.binning \
                = self.get_sci_metadata(frames[0], det)

        msgs.info("Object finding begins for {} on det={}".format(self.basename, det))

        # Is this a standard star?
        self.std_redux = 'standard' in self.objtype
        frame_par = self.par['calibrations']['standardframe'] if self.std_redux else self.par['scienceframe']
        # Get the standard trace if need be

        if self.std_redux is False and std_outfile is not None:
            std_trace = specobjs.get_std_trace(self.spectrograph.get_det_name(det), std_outfile)
        else:
            std_trace = None

        # Build Science image
        sci_files = self.fitstbl.frame_paths(frames)
        sciImg = buildimage.buildimage_fromlist(
            self.spectrograph, det, frame_par,
            sci_files, bias=self.caliBrate.msbias, bpm=self.caliBrate.msbpm,
            dark=self.caliBrate.msdark,
            flatimages=self.caliBrate.flatimages,
            slits=self.caliBrate.slits,  # For flexure correction
            ignore_saturation=False)

        # Background Image?
        if len(bg_frames) > 0:
            bg_file_list = self.fitstbl.frame_paths(bg_frames)
            sciImg = sciImg.sub(
                buildimage.buildimage_fromlist(
                self.spectrograph, det, frame_par,bg_file_list,
                bpm=self.caliBrate.msbpm, bias=self.caliBrate.msbias,
                dark=self.caliBrate.msdark,
                flatimages=self.caliBrate.flatimages,
                slits=self.caliBrate.slits,  # For flexure correction
                ignore_saturation=False), frame_par['process'])

        # Deal with manual extraction
        row = self.fitstbl[frames[0]]
        manual_obj = ManualExtractionObj.by_fitstbl_input(
            row['filename'], row['manual'], self.spectrograph) if len(row['manual'].strip()) > 0 else None

        # Instantiate Reduce object
        # Required for pypeline specific object
        # At instantiaton, the fullmask in self.sciImg is modified
        objFind = find_objects.FindObjects.get_instance(sciImg, self.spectrograph,
                                                        self.par, self.caliBrate,
                                                        self.objtype,
                                                        bkg_redux=self.bkg_redux,
                                                        manual=manual_obj,
                                                        find_negative=self.find_negative,
                                                        std_redux=self.std_redux,
                                                        show=self.show,
                                                        basename=self.basename)

        # Do it
        initial_sky, sobjs_obj = objFind.run(std_trace=std_trace, show_peaks=self.show)
        # Return
        return initial_sky, sobjs_obj, sciImg, objFind

    def extract_one(self, frames, det, sciImg, objFind, initial_sky, sobjs_obj):
        """
        Extract Objects in a single exposure/detector pair

        sci_ID and det need to have been set internally prior to calling this method

        Args:
            frames (:obj:`list`):
                List of frames to extract; stacked if more than one
                is provided
            det (:obj:`int`):
                Detector number (1-indexed)
            sciImg (:class:`PypeItImage`):
                Data container that holds a single image from a
                single detector its related images (e.g. ivar, mask)
            objFind : :class:`~pypeit.find_objects.FindObjects`
                Object finding object
            initial_sky (`numpy.ndarray`_):
                Initial global sky model
            sobjs_obj (:class:`pypeit.specobjs.SpecObjs`):
                List of objects found during `run_objfind`

        Returns:
            tuple: Returns six `numpy.ndarray`_ objects and a
            :class:`pypeit.specobjs.SpecObjs` object with the
            extracted spectra from this exposure/detector pair. The
            six `numpy.ndarray`_ objects are (1) the science image,
            (2) its inverse variance, (3) the sky model, (4) the
            object model, (5) the model inverse variance, and (6) the
            mask.
        """
        # Grab some meta-data needed for the reduction from the fitstbl
        self.objtype, self.setup, self.obstime, self.basename, self.binning \
                = self.get_sci_metadata(frames[0], det)
        # Is this a standard star?
        self.std_redux = 'standard' in self.objtype

        # Update the skymask
        skymask = objFind.create_skymask(sobjs_obj)
        # Update the global sky
        if 'standard' in self.fitstbl['frametype'][frames[0]] or \
                self.par['reduce']['findobj']['skip_final_global'] or \
                self.par['reduce']['skysub']['load_mask'] or \
                self.par['reduce']['skysub']['user_regions'] is not None:
            final_global_sky = initial_sky
        else:
            final_global_sky = objFind.global_skysub(previous_sky=initial_sky, skymask=skymask, show=self.show)
        scaleImg = objFind.scaleimg

        # update here slits.mask since global_skysub modify reduce_bpm and we need to propagate it into extraction
        flagged_slits = np.where(objFind.reduce_bpm)[0]
        if len(flagged_slits) > 0:
            self.caliBrate.slits.mask[flagged_slits] = \
                self.caliBrate.slits.bitmask.turn_on(self.caliBrate.slits.mask[flagged_slits], 'BADREDUCE')

        msgs.info("Extraction begins for {} on det={}".format(self.basename, det))

        # Instantiate Reduce object
        # Required for pypeline specific object
        # At instantiaton, the fullmask in self.sciImg is modified
        # TODO Are we repeating steps in the init for FindObjects and Extract??
        self.exTract = extraction.Extract.get_instance(
            sciImg, sobjs_obj, self.spectrograph, 
            self.par, self.caliBrate, self.objtype, 
            bkg_redux=self.bkg_redux,
            return_negative=self.par['reduce']['extraction']['return_negative'],
            std_redux=self.std_redux,
            show=self.show,
            basename=self.basename)

        if not self.par['reduce']['extraction']['skip_extraction']:
            skymodel, objmodel, ivarmodel, outmask, sobjs, waveImg, \
                tilts = self.exTract.run(final_global_sky, ra=self.fitstbl["ra"][frames[0]],
                                         dec=self.fitstbl["dec"][frames[0]], obstime=self.obstime)
        else:
            # Although exrtaction is not performed, still need to prepare some masks and the tilts
            self.exTract.prepare_extraction()
            # Since the extraction was not performed, fill the arrays with the best available information
            skymodel = final_global_sky
            objmodel = np.zeros_like(self.exTract.sciImg.image)
            ivarmodel = np.copy(self.exTract.sciImg.ivar)
            outmask = self.exTract.sciImg.fullmask
            waveImg = self.exTract.waveimg
            tilts = self.exTract.tilts
            sobjs = sobjs_obj

        # TODO -- Do this upstream
        # Tack on detector and wavelength RMS
        for sobj in sobjs:
            sobj.DETECTOR = sciImg.detector
            iwv = np.where(self.caliBrate.wv_calib.spat_ids == sobj.SLITID)[0][0]
            sobj.WAVE_RMS =self.caliBrate.wv_calib.wv_fits[iwv].rms

        # Construct table of spectral flexure
        spec_flex_table = Table()
        spec_flex_table['spat_id'] = self.caliBrate.slits.spat_id
        spec_flex_table['sci_spec_flexure'] = self.exTract.slitshift

        # pull out maskdef_designtab from caliBrate.slits
        maskdef_designtab = self.caliBrate.slits.maskdef_designtab
        slits = copy.deepcopy(self.caliBrate.slits)
        slits.maskdef_designtab = None

        # Construct the Spec2DObj
        spec2DObj = spec2dobj.Spec2DObj(sciimg=sciImg.image,
                                        ivarraw=sciImg.ivar,
                                        skymodel=skymodel,
                                        objmodel=objmodel,
                                        ivarmodel=ivarmodel,
                                        scaleimg=scaleImg,
                                        waveimg=waveImg,
                                        bpmmask=outmask,
                                        detector=sciImg.detector,
                                        sci_spat_flexure=sciImg.spat_flexure,
                                        sci_spec_flexure=spec_flex_table,
                                        vel_corr=self.exTract.vel_corr,
                                        vel_type=self.par['calibrations']['wavelengths']['refframe'],
                                        tilts=tilts,
                                        slits=slits,
                                        wavesol=self.caliBrate.wv_calib.wave_diagnostics(print_diag=False),
                                        maskdef_designtab=maskdef_designtab)
        spec2DObj.process_steps = sciImg.process_steps

        # QA
        spec2DObj.gen_qa()

        # Return
        return spec2DObj, sobjs

    def save_exposure(self, frame, all_spec2d, all_specobjs, basename, history=None):
        """
        Save the outputs from extraction for a given exposure

        Args:
            frame (:obj:`int`):
                0-indexed row in the metadata table with the frame
                that has been reduced.
            all_spec2d(:class:`pypeit.spec2dobj.AllSpec2DObj`):
            sci_dict (:obj:`dict`):
                Dictionary containing the primary outputs of
                extraction
            basename (:obj:`str`):
                The root name for the output file.
            history (:obj:`pypeit.history.History`):
                History entries to be added to fits header
        Returns:
            None or SpecObjs:  All of the objects saved to disk

        """
        # TODO: Need some checks here that the exposure has been reduced?

        # Determine the headers
        row_fitstbl = self.fitstbl[frame]
        # Need raw file header information
        rawfile = self.fitstbl.frame_paths(frame)
        head2d = fits.getheader(rawfile, ext=self.spectrograph.primary_hdrext)

        # Check for the directory
        if not os.path.isdir(self.science_path):
            os.makedirs(self.science_path)

        # NOTE: There are some gymnastics here to keep from altering
        # self.par['rdx']['detnum'].  I.e., I can't just set update_det =
        # self.par['rdx']['detnum'] because that can alter the latter if I don't
        # deepcopy it...
        if self.par['rdx']['detnum'] is None:
            update_det = None
        elif isinstance(self.par['rdx']['detnum'], list):
            update_det = [self.spectrograph.allowed_mosaics.index(d)+1 
                            if isinstance(d, tuple) else d for d in self.par['rdx']['detnum']]
        else:
            update_det = self.par['rdx']['detnum']

        subheader = self.spectrograph.subheader_for_spec(row_fitstbl, head2d)
        # 1D spectra
        if all_specobjs.nobj > 0:
            # Spectra
            outfile1d = os.path.join(self.science_path, 'spec1d_{:s}.fits'.format(basename))
            # TODO
            #embed(header='deal with the following for maskIDs;  713 of pypeit')
            all_specobjs.write_to_fits(subheader, outfile1d,
                                       update_det=update_det,
                                       slitspatnum=self.par['rdx']['slitspatnum'],
                                       history=history)
            # Info
            outfiletxt = os.path.join(self.science_path, 'spec1d_{:s}.txt'.format(basename))
            # TODO: Note we re-read in the specobjs from disk to deal with situations where
            # only a single detector is run in a second pass but in the same reduction directory.
            # Thiw was to address Issue #1116 in PR #1154. Slightly inefficient, but only other
            # option is to re-work write_info to also "append"
            sobjs = specobjs.SpecObjs.from_fitsfile(outfile1d, chk_version=False)
            sobjs.write_info(outfiletxt, self.spectrograph.pypeline)
            #all_specobjs.write_info(outfiletxt, self.spectrograph.pypeline)

        # 2D spectra
        outfile2d = os.path.join(self.science_path, 'spec2d_{:s}.fits'.format(basename))
        # Build header
        pri_hdr = all_spec2d.build_primary_hdr(head2d, self.spectrograph,
                                               redux_path=self.par['rdx']['redux_path'],
                                               master_key_dict=self.caliBrate.master_key_dict,
                                               master_dir=self.caliBrate.master_dir,
                                               subheader=subheader,
                                               history=history)

        # Write
        all_spec2d.write_to_fits(outfile2d, pri_hdr=pri_hdr,
                                 update_det=update_det,
                                 slitspatnum=self.par['rdx']['slitspatnum'])

    def msgs_reset(self):
        """
        Reset the msgs object
        """

        # Reset the global logger
        msgs.reset(log=self.logname, verbosity=self.verbosity)
        msgs.pypeit_file = self.pypeit_file

    def print_end_time(self):
        """
        Print the elapsed time
        """
        # Capture the end time and print it to user
        msgs.info(utils.get_time_string(time.time()-self.tstart))

    # TODO: Move this to fitstbl?
    def show_science(self):
        """
        Simple print of science frames
        """
        indx = self.fitstbl.find_frames('science')
        print(self.fitstbl[['target','ra','dec','exptime','dispname']][indx])

    def __repr__(self):
        # Generate sets string
        return '<{:s}: pypeit_file={}>'.format(self.__class__.__name__, self.pypeit_file)


