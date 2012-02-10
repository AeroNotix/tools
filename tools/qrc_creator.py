#!/usr/bin/python2

import argparse
import optparse
import os

from argument import Argument


class IgnoredFileError(Exception):
    pass

parser = argparse.ArgumentParser()

args = [Argument('dir', type=str, required=True,
                 help="Directory to create qrc file from"),

        Argument('ignore', type=str,
                 help="list of file types to ignore", nargs='*'),

        Argument('prefix', type=str, default='\t\t<file alias=',
                 help="prefix each entry with a string"),

        Argument('suffix', type=str, default= '</file>\n',
                 help="prefix each entry with a string"),

        Argument('header', type=str,
                 default='<!DOCTYPE RCC>\n<RCC version="1.0">\n\t<qresource>\n',
                 help="outputfile header", nargs='*'),

        Argument('close', type=str,
                 default='\t</qresource>\n</RCC>\n',
                 help="outputfile header"),

        Argument('output', type=str,
                 default='qrc', help='output file type')
]

for arg in args:
    parser.add_argument(arg.name, **arg.data)

results = parser.parse_args()


# create output file in same dir as input
ofile = open(os.path.join(results.dir,
                'resource.{}'.format(results.output)), 'wb'
        )

# start writing xml headers
ofile.write(''.join(results.header))

# iterate through files, only files with extensions
# get used and html files get treat differently

for file in os.listdir(results.dir):

    try:
        if file.split('.')[-1].lower() in results.ignore:

            raise IgnoredFileError

        fname = file.split('.')[0]

        if file.split('.')[1] == 'html':
            ofile.write(
                    '\t\t{0}{1}>{2}{3}\n'.format(results.prefix[0], fname,
                                                 file, results.suffix)
                    )
        else:
            ofile.write(
                    '\t\t{0}"{1}">{2}{3}\n'.format(results.prefix, fname,
                                                   file, results.suffix)
                    )
    except IndexError:
        pass

    except IgnoredFileError:
        pass

ofile.write(results.close)
ofile.close()