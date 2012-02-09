#!/usr/bin/python2

import argparse
import optparse
import os


class IgnoredFileError(Exception):
    pass

parser = argparse.ArgumentParser()

parser.add_argument('-dir',
                    type=str,
                    required=True,
                    help="Directory to create qrc file from"
                    )

parser.add_argument('-ignore',
                    type=str,
                    required=False,
                    help="list of file types to ignore",
                    nargs='*'
                    )

results = parser.parse_args()

if len(results.dir) > 1:

    # create output file in same dir
    qrc_file = open(os.path.join(results.dir, 'qrc_resource.qrc'), 'wb')

    # start writing headers
    qrc_file.write('<!DOCTYPE RCC>\n<RCC version="1.0">\n')
    qrc_file.write('\t<qresource>\n')

    # iterate through files, only files with extensions
    # get used and html files get treat differently

    for file in os.listdir(results.dir):

        try:
            if file.split('.')[-1].lower() in results.ignore:

                raise IgnoredFileError

            fname = file.split('.')[0]

            if file.split('.')[1] == 'html':
                qrc_file.write(
                        '\t\t<file alias={0}>{1}</file>\n'.format(fname, file)
                        )

            else:
                qrc_file.write(
                       '\t\t<file alias="{0}">{1}</file>\n'.format(fname, file)
                        )

        except IndexError:
            pass

        except IgnoredFileError:
            pass

    qrc_file.write('\t</qresource>\n')
    qrc_file.write('</RCC>\n')


