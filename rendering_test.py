#!/usr/bin/python
# Copyright 2013 Nandaja Varma <nandaja.varma@gmail.com>
# http://smc.org.in
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

import sys
from sys import argv
import ConfigParser
import os
import testing_modules
from array import *


def get_path(file_name):
    # Checking error status of files
    config_dir = os.path.dirname(config_file)
    file_dir = os.path.dirname(file_name)
    if file_dir:
        file_dir = file_dir + '/'
    absolute_file_dir = os.path.join(config_dir, file_dir)
    real_file_name = file_name.split('/')[-1]
    file_path = absolute_file_dir + real_file_name
    return file_path


def open_file(file_name, descriptor):
    file_path = get_path(file_name)
    try:
        file_pointer = open(file_path, descriptor)
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


def rendering_check(ref_file, rend_output,
                    font_file, test_cases, output_file, engine):
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
    a, wordlist, check_flag, ref_file_lines, rend_file_lines = \
        testing_modules.main(ref_fp, rend_fp, test_fp)
    ref_pointer = open_file(ref_file, "r")
    rend_pointer = open_file(rend_output, "r")
    rend_lists = rend_pointer.read().split("\n")
    ref_lists = ref_pointer.read().split("\n")
    if check_flag == 1:
        print "\nRendering problems observed!\n"
        if output_file and outflag != 1:
            print "Provide an html file as output file." + \
                "Cannot generate the result. Exiting.."
            sys.exit()
        if outflag:
            if test_cases:
                # creating images if the engine is harfbuzz
                dirname = get_path('hb_images')
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
                            font_path = get_path(font_file)
                            while wordlist[i] != "":
                                cmd2 = 'hb-view ' + font_path + ' ' + \
                                    wordlist[i] + ' > ' + dirname + \
                                    '/' + '%d' % (i + 1) + '.png'
                                os.system(cmd2)
                                i = i + 1
                            font_fp.close()
                        else:
                            print "Provide a font file with .ttf extension.\
                                Cannot create harfbuzz rendered images.\n"
                    else:
                        print "No font file provided!" + \
                            "Cannot create harfbuzz rendered images.\n"
                print "\nOpen the file '" + output_file + \
                    "' in a browser to see the result\n"
                # calling function to generate the results file
                testing_modules.get_result(
                    a,
                    wordlist,
                    output_fp,
                    diflag,
                    dirname,
                    ref_file_lines,
                    rend_file_lines)
                output_fp.close()
            else:
                print "No test cases file provided! Cannot generate \
                    the result.\n"
    rend_fp.close()
    ref_fp.close()
    return 0


if __name__ == '__main__':
    try:
        config_file = sys.argv[1]
        if config_file.endswith('.ini') == 0:
            print "Provide a configuration file in ini format as the \
                argument. Exiting!.."
            sys.exit()
    except IndexError:
        print "Usage: rendering_test.py CONFIGURATION_FILE\
            \nProvide an ini file as argument"
        sys.exit()
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
    rendering_check(
        ref_file,
        rend_output,
        font_file,
        test_cases,
        output_file,
        engine)
