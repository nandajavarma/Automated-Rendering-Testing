#!/usr/bin/python
import sys
from sys import argv
import ConfigParser
import os
import testing_modules
from array import *

script, config_file = argv
# Checking error status of files


def open_file(file_name, descriptor):
    try:
        file_pointer = open(file_name, descriptor)
    except:
        print "\nCould not open the file " + file_name
        sys.exit()
    return file_pointer


def ConfigSectionMap(option):
    try:
        file_name = Config.get('main', option)
    except:
        file_name = 0
    return file_name

Config = ConfigParser.ConfigParser()
Config.read(config_file)

ref_file = ConfigSectionMap('reference-file')
rend_output = ConfigSectionMap('rendered-output')
if ref_file == 0 or rend_output == 0:
    print "No refernce file or rendered output provided.. Exiting.."
    sys.exit()
font_file = ConfigSectionMap('font-file')
test_cases = ConfigSectionMap('test-cases-file')
output_file = ConfigSectionMap('output-file')
error_file = ConfigSectionMap('error-file')
dirname = ConfigSectionMap('directory-name')
if output_file:
    output_fp = open_file(output_file, "w")
if test_cases:
    test_fp = open_file(test_cases, "r")
else:
    test_fp = 0
ref_fp = open_file(ref_file, "r")
rend_fp = open_file(rend_output, "r")
# Calling function to test the engine
a, wordlist, f = testing_modules.main(
    ref_fp, rend_fp, test_fp, error_file)
if f == 1:
    print "\nRendering problems observed!\n"
    # Creating a copy of the index of wrongly rendered words
    b = array('i', [])
    for i in a:
        b.append(i)
    if output_file:
        if test_cases:
            print "File '" + output_file + \
                "' shows the rendering status of each word\n"
            # calling function to generate the results file
            testing_modules.get_result(a, wordlist, output_fp)
            output_fp.close()
        else:
            print "No test cases file provided! Cannot create output file\n"
    if error_file:
        if test_cases:
            print "File '" + error_file + \
                "' shows the list of wrongly rendered words\n"
        else:
            print "No test cases file provided! Cannot create error file\n"
    # Assuming the engine would be harfbuzz if a directory name is provided
    if dirname:
        if font_file:
            font_fp = open_file(font_file, "r")
            cmd1 = 'mkdir ' + dirname
            os.system(cmd1)
            for i in b:
                cmd2 = 'hb-view ' + font_file + ' ' + \
                    wordlist[i] + ' > ' + dirname + \
                    '/' + '%d' % (i + 1) + '.png'
                os.system(cmd2)
            print "\nDirectory '" + dirname + \
                "' shows the images of wrongly rendered words\n"
            font_fp.close()
        else:
            print "No font file provided!" + \
                "Cannot create images of wrongly rendered words"
rend_fp.close()
ref_fp.close()
