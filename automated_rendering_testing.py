#!/usr/bin/python
import sys
import os
import testing_modules 
choice = raw_input("Automated Rendering testing.\nAre you trying to test rendering by harfbuzz?[y/n](y by default):").lower()
fontfile = raw_input("\nPath to the font file(in .ttf format):")
word_file = raw_input("\nPath to the test cases' file:")
ref_file = raw_input("\nPath to the reference file:")
if choice == 'n':
	renderingfile = raw_input("\nPath to the file containing renderings by the specified engine:")
else:
	cmd = 'hb-shape ' + fontfile + ' --text-file=' + word_file + ' > hb_rendering.txt'
	os.system(cmd)

renderingfile = "hb_rendering.txt"
ref_file_pointer = open(ref_file)
word_file_pointer = open(word_file)
rend_file_pointer = open(renderingfile)
a, wordlist = testing_modules.renderingtest(ref_file_pointer, rend_file_pointer, word_file_pointer)
testing_modules.get_result(a,wordlist,choice, fontfile)
if choice != 'n':
	cmd3 =  'hb-view ' + fontfile + '  --text-file=result.txt > output.png'
	os.system(cmd3)
	print "output.png gives the rendering mistakes by harfbuzz.\n"
ref_file_pointer.close()
rend_file_pointer.close()
word_file_pointer.close()


