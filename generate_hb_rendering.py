#!/usr/bin/python
import os
from sys import argv
import sys
import argparse
parser = argparse.ArgumentParser()
 
parser.add_argument('-t', dest='text_file', help='File with all the test cases', action='store', required=True)
parser.add_argument('-o', dest='output_file', help='File to store the harfbuzz renderings', action='store', required=True)
parser.add_argument('-f', dest= 'font_file', help='Font file in .ttf format', action='store', required=True)

args = parser.parse_args()
try:
  results = parser.parse_args()
except IOError, msg:
  parser.error(str(msg))

os.system('hb-shape --font-file=' + args.font_file + ' --text-file=' + args.text_file + ' > ' + args.output_file)
print "Harfbuzz renderings stored inside the file " + args.output_file
