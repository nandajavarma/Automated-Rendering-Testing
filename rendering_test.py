#!/usr/bin/python
import sys
import argparse
import os
import testing_modules
from array import *


# Checking error status of files
def open_file(file_name, descriptor):
    try:
        file_pointer = open(file_name, descriptor)
    except:
        print "\nCould not open the file " + file_name
        sys.exit()
    return file_pointer
parser = argparse.ArgumentParser(version='1.0')
# parsing the files passed as parameters
parser.add_argument(
    '-w',
    dest='word_file',
    help='Test cases file',
    type=argparse.FileType('rt'),
    required=True)
parser.add_argument(
    '-r',
    dest='ref_file',
    help='Reference file',
    type=argparse.FileType('rt'),
    required=True)
parser.add_argument(
    '-t',
    dest='hb_rendering',
    help='Rendering output by the engine',
    type=argparse.FileType('rt'),
    required=True)
parser.add_argument(
    '-o',
    dest='output_file',
    help='Name for output file',
    action='store',
    required=True)
parser.add_argument(
    '-e',
    dest='error_file',
    help='File to store the wrong renderings',
    action='store',
    required=True)
parser.add_argument(
    '-f',
    dest='font_file',
    help='Font file in .ttf format',
    action='store',
    required=True)
parser.add_argument(
    '-m',
    dest='dirname',
    help='Directory to store wrongly rendered harfbuzz views',
    action='store')
args = parser.parse_args()
try:
    results = parser.parse_args()
except IOError as msg:
    parser.error(str(msg))
error_fp = open_file(args.error_file, "w")
output_fp = open_file(args.output_file, "w")
# Calling function to test the engine
a, wordlist, f = testing_modules.renderingtest(
    args.ref_file, args.hb_rendering, args.word_file, error_fp)
if f == 1:
    print "\nRendering problems observed!\n"
    print args.output_file + " shows rendering status of each word.\n"
    print args.error_file + " shows the list of wrongly rendered words.\n"
# Creating a copy of the index of wrongly rendered words
    b = array('i', [])
    for i in a:
        b.append(i)
    # calling function to generate the results file
    testing_modules.get_result(a, wordlist, output_fp)
    # Assuming the engine would be harfbuzz if a directory name is provided
    if args.dirname:
        cmd1 = 'mkdir ' + args.dirname
        os.system(cmd1)
        for i in b:
            cmd2 = 'hb-view ' + args.font_file + ' ' + \
                wordlist[i] + ' > ' + args.dirname + \
                '/' + '%d' % (i + 1) + '.png'
            os.system(cmd2)
        print "\n" + args.dirname + \
            " directory gives the images of wrongly rendered words.\n"
args.word_file.close()
args.ref_file.close()
args.hb_rendering.close()
output_fp.close()
error_fp.close()
