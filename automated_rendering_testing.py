#!/usr/bin/python
import sys
import os
import testing_modules 
from array import *
choice = raw_input("Automated Rendering testing.\nAre you trying to test rendering by harfbuzz?[y/n](y by default):").lower()
fontfile = raw_input("\nPath to the font file(in .ttf format):")
word_file = raw_input("\nPath to the test cases' file:")
ref_file = raw_input("\nPath to the reference file:")
error_file = raw_input("\nName of the text file on to which the incorrectly rendered words are to be stored:")
res_file = raw_input("\nName the text file on to which the final result is to be stored:")

if choice == 'n':
	renderingfile = raw_input("\nPath to the file containing renderings by the specified engine:")
else:
	cmd = 'hb-shape ' + fontfile + ' --text-file=' + word_file + ' > hb_rendering.txt'
	os.system(cmd)

renderingfile = "hb_rendering.txt"
ref_file_pointer = open(ref_file)
word_file_pointer = open(word_file)
rend_file_pointer = open(renderingfile)
res_file_pointer = open(res_file, 'w')
a, wordlist = testing_modules.renderingtest(ref_file_pointer, rend_file_pointer, word_file_pointer, error_file, res_file)
b = array('i',[])
for i in a:
	b.append(i)
testing_modules.get_result(a, wordlist, choice, fontfile, res_file_pointer)
if choice == 'n':
	sys.exit()
directory = raw_input("\nName of the directory on which images of wrong harfbuzz renderings are to be saved:")
cmd1 = 'mkdir ' + directory
os.system(cmd1)
for i in b:
		cmd3 =  'hb-view ' + fontfile + ' ' + wordlist[i] + ' > ' +  wordlist[i] + '.png'  
		os.system(cmd3)
cmd2 = 'cp *.png ' + directory + '/.'
os.system(cmd2)
os.system('rm *.png')
print "Look inside the directory " + directory + " for the images of wrongly rendered words.\n"
ref_file_pointer.close()
rend_file_pointer.close()
word_file_pointer.close()
res_file_pointer.close()


