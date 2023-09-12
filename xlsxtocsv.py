#!/usr/bin/env python

"""
Installation:
    If the file is named `xlsxtocsv.py` then you will need to rename it to `xlsxtocsv` and then run `chmod +x xlsxtocsv`
    Simply place the file in a directory contained in your PATH
    Ensure you run `pip install -r reqs.txt`
"""
import pandas as pd 
import sys

if len(sys.argv) == 3:
    read_file = pd.read_excel(sys.argv[1])
    read_file.to_csv(sys.argv[2], index=None, header=True)
else: 
    print(f'Usage: xlsxtocsv <xlsx_file> <csv_file>')
