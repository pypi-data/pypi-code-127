"""
Launch the identify GUI tool.

.. include common links, assuming primary doc root is up one directory
.. include:: ../include/links.rst
"""
from IPython import embed

from pypeit.scripts import scriptbase

class Identify(scriptbase.ScriptBase):

    @classmethod
    def get_parser(cls, width=None):
        parser = super().get_parser(description='Launch PypeIt identify tool, display extracted '
                                                'MasterArc, and load linelist.'
                                                'Run above the Masters/ folder.', width=width)
        parser.add_argument('arc_file', type=str, default=None, help='PypeIt MasterArc file')
        parser.add_argument('slits_file', type=str, default=None, help='PypeIt MasterSlits file')
        parser.add_argument("--lamps", type=str,
                            help="Comma separated list of calibration lamps (no spaces)")
        parser.add_argument('-s', '--solution', default=False, action='store_true',
                            help="Load a wavelength solution from the arc_file (if it exists)")
        parser.add_argument("--wmin", type=float, default=3000.0, help="Minimum wavelength range")
        parser.add_argument("--wmax", type=float, default=26000.0, help="Maximum wavelength range")
        parser.add_argument("--slit", type=int, default=0,
                            help="Which slit to load for wavelength calibration")
        parser.add_argument("--det", type=int, default=1, help="Detector index")
        parser.add_argument("--rmstol", type=float, default=0.1, help="RMS tolerance")
        parser.add_argument("--fwhm", type=float, default=4., help="FWHM for line finding")
        parser.add_argument("--sigdetect", type=float, help="sigma detection for line finding")
        parser.add_argument("--pixtol", type=float, default=0.1,
                            help="Pixel tolerance for Auto IDs")
        parser.add_argument('--test', default=False, action='store_true',
                            help="Unit tests?")
        parser.add_argument("--linear", default=False, action="store_true",
                            help="Show the spectrum in linear scale? (Default: log")
        parser.add_argument('--force_save', default=False, action='store_true',
                            help="Save the solutions, despite the RMS")
        return parser

    @staticmethod
    def main(args):

        import os
        import sys

        import numpy as np
        
        from pypeit import msgs
        from pypeit import masterframe
        from pypeit.spectrographs.util import load_spectrograph
        from pypeit.core.gui.identify import Identify
        from pypeit.core.wavecal import waveio
        from pypeit.wavecalib import BuildWaveCalib, WaveCalib
        from pypeit import slittrace
        from pypeit.images.buildimage import ArcImage

        # Load the MasterArc file
        msarc = ArcImage.from_file(args.arc_file)

        # Load the spectrograph
        spec = load_spectrograph(msarc.PYP_SPEC)
        par = spec.default_pypeit_par()['calibrations']['wavelengths']

        # Get the lamp list
        if args.lamps is None:
            lamps = par['lamps']
            if lamps is None or lamps == ['use_header']:
                msgs.error('Cannot determine the lamps; use --lamps argument')
        else:
            lamps = args.lamps.split(",")
        par['lamps'] = lamps

        # Load the slits
        slits = slittrace.SlitTraceSet.from_file(args.slits_file)
        # Reset the mask
        slits.mask = slits.mask_init

        # Check if a solution exists
        solnname = masterframe.construct_file_name(WaveCalib, msarc.master_key,
                                                   master_dir=msarc.master_dir)
        wv_calib = waveio.load_wavelength_calibration(solnname) \
                        if os.path.exists(solnname) and args.solution else None

        # Load the MasterFrame (if it exists and is desired).  Bad-pixel mask
        # set to any flagged pixel in MasterArc.
        wavecal = BuildWaveCalib(msarc, slits, spec, par, lamps, binspectral=slits.binspec,
                                 det=args.det, master_key=msarc.master_key,
                                 msbpm=msarc.select_flag())
        arccen, arc_maskslit = wavecal.extract_arcs(slitIDs=[args.slit])

        # Launch the identify window
        # TODO -- REMOVE THIS HACK
        try:
            nonlinear_counts = msarc.detector.nonlinear_counts()
        except AttributeError:
            nonlinear_counts = None
        arcfitter = Identify.initialise(arccen, lamps, slits, slit=int(args.slit), par=par,
                                        wv_calib_all=wv_calib, wavelim=[args.wmin, args.wmax],
                                        nonlinear_counts=nonlinear_counts,
                                        pxtoler=args.pixtol, test=args.test, 
                                        fwhm=args.fwhm,
                                        sigdetect=args.sigdetect,
                                        specname=spec.name, y_log=not args.linear)

        # Testing?
        if args.test:
            return arcfitter
        final_fit = arcfitter.get_results()

        # Build here to avoid circular import
        #  Note:  This needs to be duplicated in test_scripts.py
        # Wavecalib (wanted when dealing with multiple detectors, eg. GMOS)
        if 'WaveFit' in arcfitter._fitdict.keys():
            waveCalib = WaveCalib(nslits=1, wv_fits=np.atleast_1d(arcfitter._fitdict['WaveFit']),
                                  arc_spectra=np.atleast_2d(arcfitter.specdata).T,
                                  spat_ids=np.atleast_1d(int(arcfitter._spatid)), PYP_SPEC=msarc.PYP_SPEC,
                                  lamps=','.join(lamps))
        else:
            waveCalib = None

        # Ask the user if they wish to store the result in PypeIt calibrations
        arcfitter.store_solution(final_fit, slits.binspec,
                                 wvcalib=waveCalib,
                                 rmstol=args.rmstol,
                                 force_save=args.force_save)


