"""
This script enables the user to convert spec2D FITS files
from IFU instruments into a 3D cube with a defined WCS.

.. include common links, assuming primary doc root is up one directory
.. include:: ../include/links.rst
"""
import time
from pypeit import msgs
from pypeit import par
from pypeit import io
from pypeit import inputfiles
from pypeit import utils
from pypeit.core.datacube import coadd_cube
from pypeit.spectrographs.util import load_spectrograph
from pypeit.scripts import scriptbase


class CoAddDataCube(scriptbase.ScriptBase):

    @classmethod
    def get_parser(cls, width=None):
        parser = super().get_parser(description='Read in an array of spec2D files and convert '
                                                'them into a datacube', width=width)
        parser.add_argument('file', type = str, default=None, help='filename.coadd3d file')
        parser.add_argument('--det', default=1, type=int, help="Detector")
        parser.add_argument('-o', '--overwrite', default=False, action='store_true',
                            help='Overwrite any existing files/directories')
        return parser

    @staticmethod
    def main(args):
        # Check that a file has been provided
        if args.file is None:
            msgs.error('You must input a coadd3d file')

        # Read in the relevant information from the .coadd3d file
        coadd3dfile = inputfiles.Coadd3DFile.from_file(args.file)
        spectrograph = load_spectrograph(coadd3dfile.config['rdx']['spectrograph'])

        # Parameters
        spectrograph_def_par = spectrograph.default_pypeit_par()
        parset = par.PypeItPar.from_cfg_lines(cfg_lines=spectrograph_def_par.to_config(),
                                              merge_with=coadd3dfile.cfg_lines)
        # If detector was passed as an argument override whatever was in the coadd3d file
        if args.det is not None:
            msgs.info("Restricting to detector={}".format(args.det))
            parset['rdx']['detnum'] = int(args.det)

        # Coadd the files
        tstart = time.time()
        coadd_cube(coadd3dfile.filenames, coadd3dfile.options, parset=parset, overwrite=args.overwrite)
        msgs.info(utils.get_time_string(time.time()-tstart))
