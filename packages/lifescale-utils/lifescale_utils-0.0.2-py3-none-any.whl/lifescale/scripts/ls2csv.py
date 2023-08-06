"""Converstion program from xlsm to csv

Copyright (C) 2022  Andreas Hellerschmied <heller182@gmx.at>"""

from lifescale.models.ls_data import LSData


def ls2csv(xlsm_filename, oputput_dir, verbose=True):
    """Convert lifescale output file (xlsm) to csv files."""
    ls_data = LSData.from_xlsm_file(input_xlsm_filename=xlsm_filename, verbose=verbose)
    ls_data.export_csv_files(oputput_dir, verbose=verbose)
