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
    type=argparse.FileType('rt'))
parser.add_argument(
    '-r',
    dest='ref_file',
    help='Reference file',
    type=argparse.FileType('rt'),
    required=True)
parser.add_argument(
    '-t',
    dest='rendered_output',
    help='Rendering output by the engine',
    type=argparse.FileType('rt'),
    required=True)
parser.add_argument(
    '-o',
    dest='output_file',
    help='Name for output file',
    action='store')
parser.add_argument(
    '-e',
    dest='error_file',
    help='File to store the wrong renderings',
    action='store')
parser.add_argument(
    '-f',
    dest='font_file',
    help='Font file in .ttf format',
    action='store')
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
if args.output_file:
    output_fp = open_file(args.output_file, "w")
# Calling function to test the engine
a, wordlist, f = testing_modules.main(
    args.ref_file, args.rendered_output, args.word_file, args.error_file)
if f == 1:
    print "\nRendering problems observed!\n"
    # Creating a copy of the index of wrongly rendered words
    b = array('i', [])
    for i in a:
        b.append(i)
    if args.output_file:
        if args.word_file:
            print "File '" + args.output_file + "' shows the rendering status of each word\n"
            # calling function to generate the results file
            testing_modules.get_result(a, wordlist, output_fp)
            output_fp.close()
        else:
            print "No test cases file provided! Cannot create output file\n"
    if args.error_file:
        if args.word_file:
            print "File '" + args.error_file + "' shows the list of wrongly rendered words\n"
        else:
            print "No test cases file provided! Cannot create error file\n"
    # Assuming the engine would be harfbuzz if a directory name is provided
    if args.dirname:
        if args.font_file:
            cmd1 = 'mkdir ' + args.dirname
            os.system(cmd1)
            for i in b:
                cmd2 = 'hb-view ' + args.font_file + ' ' + \
                    wordlist[i] + ' > ' + args.dirname + \
                    '/' + '%d' % (i + 1) + '.png'
                os.system(cmd2)
            print "\nDirectory '" + args.dirname + \
                "' shows the images of wrongly rendered words\n"
        else:
            print "No font file provided! Cannot create images of words rendered wrongly"  
args.ref_file.close()
args.rendered_output.close()
