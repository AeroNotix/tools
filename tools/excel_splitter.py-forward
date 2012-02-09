#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import xlwt
import argparse
from utility import openxls, get_headings
from argument import Argument

__author__ = 'Aaron France'
__email__ = 'aaron.l.france@gmail.com'

parser = argparse.ArgumentParser()


"""
def __init__(self, choices=None, required=False, help='',type=str
"""

args = [
       Argument('input', help="File to change", required=True),
       Argument('type', help="type of split",
                choices=['filesplit', 'sheetsplit'], required=True),
                
       Argument('row', help="row to perform split on",type=int,required=True),
       Argument('output', help="output file", requireds=True)
]
      



for arg in args:
    parser.add_argument(arg.name, **arg.data)

results = parser.parse_args()

print get_headings(openxls(results.input, atpage=0))


