""" Command line interface of lifescale utils

Copyright (C) 2022  Andreas Hellerschmied <heller182@gmx.at>
"""

from lifescale.scripts.ls2csv import ls2csv as ls2csv_main
import argparse
import os


def is_file(filename):
    """Check, whether the input string is the path to an existing file."""
    if os.path.isfile(filename):
        return filename
    raise argparse.ArgumentTypeError("'{}' is not a valid file.".format(filename))


def is_dir(pathname):
    """Check, whether the input string is a valid and existing filepath."""
    if os.path.exists(pathname):
        return pathname
    raise argparse.ArgumentTypeError("'{}' is not a valid directory.".format(pathname))


def ls2csv():
    """Command line interface including argument parser for the lifescale2csv converter."""
    parser = argparse.ArgumentParser(prog="ls2csv",
                                     description="Covnersion from lifescale xlsm output to csv files",
                                     epilog="The ls2csv converter loads and parses xslm files created by the lifescale "
                                            "unit. It writes several csv files to the output directory that contain "
                                            "extraced data from the input xlsm file in an easily readable way.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input-xlsm", type=is_file, required=True, help="Path and name of the input xlsm file created by "
                                                                 "lifescale.")
    parser.add_argument("-o", "--out-dir", type=is_dir, required=True, help="Output directory for the CSV files.")
    parser.add_argument("-nv", "--not-verbose", required=False, help="Disable command line status messages.",
                        action='store_true')
    # parser.add_argument("--out-dir", type=is_dir, required=False,
    #                     help="path to output directory", default=OUT_PATH)
    args = parser.parse_args()
    verbose = not args.not_verbose

    return ls2csv_main(xlsm_filename=args.input_xlsm, oputput_dir=args.out_dir, verbose=verbose)


if __name__ == '__main__':
    ls2csv()


