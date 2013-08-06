#!/usr/bin/python
import sys
import os
import testing_modules 
from array import *
os.system('clear')
#Function to check if the file opens correctly
def open_file(file_name, descriptor):
	try:
		file_pointer = open(file_name, descriptor)
	except:
		print "Could not open the file " + file_name
		sys.exit()
	return file_pointer
def framework():
	choice = raw_input("\n\t\tAutomated Rendering testing\n \t\t---------------------------\nAre you trying to test rendering by harfbuzz?[y/n](y by default): ").lower()
	fontfile = raw_input("\nPath to the font file(in .ttf format): ")
	font_file_pointer = open_file(fontfile, 'r')
	word_file = raw_input("\nPath to the test cases' file: ")
	word_file_pointer = open_file(word_file, 'r')
	ref_file = raw_input("\nPath to the reference file: ")
	ref_file_pointer = open_file(ref_file, 'r')
	error_file = raw_input("\nName of the text file on to which the incorrectly rendered words are to be stored: ")
	error_file_pointer = open_file(error_file, 'w')
	res_file = raw_input("\nName the text file on to which the final result is to be stored: ")
	res_file_pointer = open_file(res_file, 'w')
	#Option for engines other than harfbuzz
	if choice == 'n':
		renderingfile = raw_input("\nPath to the file containing renderings by the specified engine: ")
	else:
		cmd = 'hb-shape ' + fontfile + ' --text-file=' + word_file + ' > hb_rendering.txt'
		os.system(cmd)
		renderingfile = "hb_rendering.txt"
	rend_file_pointer = open_file(renderingfile, 'r')
	#Calling function to test renderings
	a, wordlist, f = testing_modules.renderingtest(ref_file_pointer, rend_file_pointer, word_file_pointer, error_file_pointer)
	if f == 1:
	 	print "\nRendering problems observed!\nSee the file " + res_file + " for rendering status of each word and " + error_file + " for the list of wrongly rendered words only.\n"
	b = array('i',[])
	for i in a:
		b.append(i)
	#calling function to generate the results file
	testing_modules.get_result(a, wordlist, choice, fontfile, res_file_pointer)
	if choice == 'n':
		sys.exit()
	#Storing the wrong renderings' images in a specified directory
	directory = raw_input("\nName of the directory on which images of wrong harfbuzz renderings are to be saved: ")
	cmd1 = 'mkdir ' + directory
	os.system(cmd1)
	for i in b:
		cmd2 =  'hb-view ' + fontfile + ' ' + wordlist[i] + ' > ' + directory + '/' + '%d' % (i + 1) + '.png'  
		os.system(cmd2)
	print "\n\nLook inside the directory " + directory + " for the images of wrongly rendered words.\n"
	ref_file_pointer.close()
	rend_file_pointer.close()
	word_file_pointer.close()
	res_file_pointer.close()
	error_file_pointer.close()
	font_file_pointer.close()
	return

if __name__  == '__main__':
	framework()
