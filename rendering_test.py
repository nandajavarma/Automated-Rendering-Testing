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
engine = ConfigSectionMap('shaping-engine')
hbflag = 0
if engine:
    if engine.lower() == 'harfbuzz':
        hbflag = 1
outflag = 0
if output_file:
    if output_file.endswith('.html'):
        outflag = 1
        output_fp = open_file(output_file, "w")
if test_cases:
    test_fp = open_file(test_cases, "r")
else:
    test_fp = 0
ref_fp = open_file(ref_file, "r")
rend_fp = open_file(rend_output, "r")
# Calling function to test the engine
a, wordlist, f = testing_modules.main(
    ref_fp, rend_fp, test_fp)
if f == 1:
    print "\nRendering problems observed!\n"
    if output_file and outflag != 1:
        print "Provide an html file as output file." + \
            "Cannot generate the result. Exiting.."
        sys.exit()
    if outflag:
        if test_cases:
            #creating images if the engine is harfbuzz
            dirname = 'hb_images'
            diflag = 0
            if hbflag:
                if font_file:
                    if font_file.endswith('.ttf'):
                        diflag = 1
                        font_fp = open_file(font_file, "r")
                        if os.path.isdir(dirname):
                            cmd0 = 'rm -rf ' + dirname
                            os.system(cmd0)
                        cmd1 = 'mkdir ' + dirname
                        os.system(cmd1)
                        i = 0
                        print "\nProcessing...."
                        while wordlist[i] != "":
                            cmd2 = 'hb-view ' + font_file + ' ' + \
                                wordlist[i] + ' > ' + dirname + \
                                '/' + '%d' % (i + 1) + '.png'
                            os.system(cmd2)
                            i = i + 1
                        font_fp.close()
                    else:
                        print "Provide a font file with .ttf extension." + \
                            "Cannot create harfbuzz rendered images.\n"
                else:
                    print "No font file provided!" + \
                        "Cannot create harfbuzz rendered images.\n"
            print "\nOpen the file '" + output_file + \
                        "' in a browser to see the result\n"
            # calling function to generate the results file
            testing_modules.get_result(a, wordlist, output_fp, diflag, dirname)
            output_fp.close()
        else:
            print "No test cases file provided! Cannot generate the result.\n"
rend_fp.close()
ref_fp.close()
