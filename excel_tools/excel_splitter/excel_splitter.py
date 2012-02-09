import xlrd
import xlwt
import argparse
from argument import Argument

args = [
       Argument(name='file',help='input filename'),
       Argument(name='type',help='Conversion type',choices=['same','separate']),
       Argument(name='output', help='Output filename'),
       Argument(name='row', help='Row to perform conversion with')
]


parser = argparse.ArgumentParser(
                          description="""
                                      Splits Excel files into
                                      files or sheets, depending
                                      on the options supplied
                                      """,

                              epilog="""
                                     All four options required
                                     """
                  )

for arg in args:
    parser.add_argument(arg.name, **arg.data)

results = parser.parse_args()

