#!/usr/bin/env python

import csv
import os

DATADIR = "/Users/sarbjitgahra/python_scripts"
DATAFILE = "745090.csv"


def parse_file(datafile):
    name = ""
    data = []
    with open(datafile,'rb') as f:
        reader = csv.reader(f)
        first_line = next(reader)
        name = first_line[1]
        next(reader)
       # print name
        for d in reader:

            data.append(d)
    # Do not change the line below
    return (name, data)

parse_file(DATAFILE)
def test():

    datafile = os.path.join(DATADIR, DATAFILE)
    name, data = parse_file(datafile)
    assert name == "MOUNTAIN VIEW MOFFETT FLD NAS"
    assert data[0][1] == "01:00"
    assert data[2][0] == "01/01/2005"
    assert data[2][5] == "2"
    print" all tests passed"
#datafile = os.path.join(DATADIR, DATAFILE)

if __name__ == "__main__":
    test()
