#!/usr/bin/python
import sys
import argparse
import os
import testing_modules
from array import *

def open_file(file_name, descriptor):
  try:
    file_pointer = open(file_name, descriptor)
  except:
    print "\nCould not open the file " + file_name 
    sys.exit()
  return file_pointer
parser = argparse.ArgumentParser(version='1.0')

parser.add_argument('-w', dest='word_list_file', help='File with all the words', type=argparse.FileType('rt'), required=True)
parser.add_argument('-r', dest='reference_file', help='Reference file for the specified font', type=argparse.FileType('rt'), required=True)
parser.add_argument('-t', dest='rendered_output_file', help='File with the output of rendering engine', type=argparse.FileType('rt'), required=True)
parser.add_argument('-o', dest='output_file', help='File to store the output', action='store')
parser.add_argument('-e', dest='error_file', help='File to store the wrong renderings', action='store')
parser.add_argument('-f', dest= 'font_file', help='Font file in .ttf format', action='store')
parser.add_argument('-m', dest='dirname', help='Directory to store images of wrong renderings if the engine is harfbuzz', action='store')
args = parser.parse_args()
try:
	results = parser.parse_args()
except IOError, msg:
	parser.error(str(msg))
error_file_pointer = open_file(args.output_file, "w")
output_file_pointer = open_file(args.output_file, "w")
a, wordlist, f = testing_modules.renderingtest(args.reference_file, args.rendered_output_file, args.word_list_file, error_file_pointer)
if f == 1:
  print "\nRendering problems observed!\nSee the file " + args.output_file + " for rendering status of each word and " + args.error_file + " for the list of wrongly rendered words only.\n"
  b = array('i',[])
  for i in a:
    b.append(i)
  #calling function to generate the results file
  testing_modules.get_result(a, wordlist, output_file_pointer)
  if args.dirname:
    cmd1 = 'mkdir ' + args.dirname
    os.system(cmd1)
    for i in b:
      cmd2 =  'hb-view ' + args.font_file + ' ' + wordlist[i] + ' > ' + args.dirname + '/' + '%d' % (i + 1) + '.png'
      os.system(cmd2)
    print "\n\nLook inside the directory " + args.dirname + " for the images of wrongly rendered words.\n"
args.word_list_file.close()
args.reference_file.close()
args.rendered_output_file.close()
output_file_pointer.close()
error_file_pointer.close()


