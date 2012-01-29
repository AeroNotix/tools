#!/usr/bin/python2

import argparse
import optparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-dir', type=str)
results = parser.parse_args()

if results.dir is None:
    print 'Usage:\n\tqrc_creator -dir "dirname"'
    quit()

if len(results.dir) > 1:

    # create output file in same dir
    qrc_file = open(os.path.join(results.dir, 'qrc_resource.qrc'), 'wb')

    # start writing headers
    qrc_file.write('<!DOCTYPE RCC><RCC version="1.0">\n')
    qrc_file.write('<qresource>\n')

    # iterate through files, only files with extensions
    # get used and html files get treat differently
    try:
        for file in os.listdir(results.dir):

            fname = file.split('.')[0]            
            if file.split('.')[1] == 'html':
                qrc_file.write('<file alias={0}>{1}</file>\n'.format(fname, file))
            else:
                qrc_file.write('<file alias="{0}">{1}</file>\n'.format(fname, file))
                
    except IndexError:
        pass
        
    qrc_file.write('</qresource>\n')
    qrc_file.write('</RCC>\n')


