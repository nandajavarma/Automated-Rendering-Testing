#!/usr/bin/python
import sys
import os
import codecs
from sys import argv
from array import *
def renderingtest(ref_file_pointer, rend_file_pointer, word_file_pointer):
	result_file = open("result.txt", 'w')
	reference_file = ref_file_pointer.read()
	rendered_file = rend_file_pointer.read()
	ref_list = []
	rend_list = []
	#Parsing the reference file
	ref_lines = reference_file.replace('[','').replace(']','')
	clean_file = ref_lines.split('\n')
	for aline in clean_file:
		aword = aline.split(',')		
		ref_list.append(aword)
	#Parsing the harfbuzz renderings' file
	rend_lines = rendered_file.replace('[','').replace(']','') 
	rend_file_lines = rend_lines.split('\n')
	for line in rend_file_lines:
		each_name = line.split('|')
		rend_list.append(each_name)
	rendered_output = []
	for x in rend_list:
		n = []
		for y in x:
			n.append(y.split('=')[0])
		rendered_output.append(n)
	#Opening the file with test cases
	wordfile_content = word_file_pointer.read()
	wordlist = []
	wordlist = wordfile_content.split('\n')
	#Matching rendered glyph names with the reference glyph names
	result_list = []
	result_list = [i for i, j in zip(ref_list, rendered_output) if i != j]
	if result_list == []:
		print "\nNo rendering problems found!"
		sys.exit()
	else:
		print "\nRendering problems detected.\nSee the file test_result.txt for rendering status of each word.\n"
		a = array('i', [])
	#Finding the wrongly rendered words from the test cases file and writing it to result.txt
		for word in result_list:	
			d = ref_list.index(word)
			result_file.write(wordlist[d] + '\n')
			a.append(d)
	result_file.close()
	return a, wordlist

def main():
	if len(argv) != 4:
		print "Correct usage is: ./rendering_testing.py	/path/to/fontfile /path/to/testcases /path/to/referencefile"
		sys.exit()
	script, fontfile, word_file, ref_file = argv
	ref_file_pointer = open(ref_file)
	word_file_pointer = open(word_file)
	choice = raw_input("\nDo you want to test the rendering with harfbuzz engine? [y/n] (y by default):").lower()
	if choice == 'n':
		renderingfile = raw_input("\nName of the file with the rendering engine output of the chosen test cases:")
		rend_file_pointer = open(renderingfile)
	else:
		#Creating a file hb_rendering.txt with harfbuzz rendering of the provided test cases file in provided font
		cmd = 'hb-shape ' + fontfile + ' --text-file=' + word_file + ' > hb_rendering.txt'
		os.system(cmd)
		rend_file_pointer = open("hb_rendering.txt")	
	#Function to test rendering testing
	a, wordlist = renderingtest(ref_file_pointer, rend_file_pointer, word_file_pointer) 
	#Generating a file test_result.txt with all test cases and its rendering status
	test_file = open("test_result.txt", 'w')
	test_file.write("Number\tWord\t\t\tRendering status\n\n")
	j = 1	
	res = array('i', [])
	for rline in wordlist:
		flag = 0
		k =  wordlist.index(rline)
		for i in a:
			if k == i:
				flag = 1
				a.remove(i)
				break
		if flag:
			res.insert(k, 1) 
		else:
			res.insert(k, 0)
		test_file.write('%d' % (j))
		if res[j - 1 ] == 1:
			test_file.write('\t'+ rline + '\t\t\t' + "Rendering is wrong" + '\n')
		else:
			test_file.write('\t' + rline + '\t\t\t' + "Rendering is correct" + '\n')
		j = j + 1
	#Generating an image file output.png with the words that are wrongly rendered
	
	res_file = codecs. open('test_result.txt', encoding = 'utf-8', errors = 'ignore')
	read_result = res_file.read()
	k = 1
	for oneline in read_result.split('\n'):
		for oneword in oneline:
			cmd2 = 'hb-view ' + fontfile + ' ' + oneword + ' > %d' % k + '.png'
			k = k + 1
			os.system(cmd2)	
	ref_file_pointer.close()
	rend_file_pointer.close()
	word_file_pointer.close()
	test_file.close()
#	res_file.close()
	return 0
main()
