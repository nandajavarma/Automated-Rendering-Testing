#!/usr/bin/python
import sys
import os
from sys import argv
def renderingtest(op, tp, wp):
	result_file = open("result.txt", 'w')
	reference_file = op.read()
	rendered_file = tp.read()
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
	wordfile_content = wp.read()
	wordlist = []
	wordlist = wordfile_content.split('\n')
	#Matching rendered glyph names with the reference glyph names
	result_list = []
	result_list = [i for i, j in zip(ref_list, rendered_output) if i != j]
	if result_list == []:
		print "No rendering problems found"
		return
	else:
		print "Rendering problems detected. Wrongly rendered texts can be found inside result.txt or output.png\n"
	#Finding the wrongly rendered words from the test cases file and writing it to result.txt
		for word in result_list:	
			d = ref_list.index(word)
			result_file.write(wordlist[d] + '\n')
	result_file.close()
	return 

def main():
	if len(argv) != 4:
		print "Correct usage is: ./rendering_testing.py	/path/to/fontfile /path/to/testcases /path/to/referencefile"
		sys.exit()
	script, fontfile, word_file, ref_file = argv
	op = open(ref_file)
	wp = open(word_file)
	#Creating a file hb_rendering.txt with harfbuzz rendering of the provided test cases file in provided font
	cmd = 'hb-shape ' + fontfile + ' --text-file=' + word_file + ' > hb_rendering.txt'
	os.system(cmd)
	tp = open("hb_rendering.txt")	
	renderingtest(op, tp, wp) #Function to test rendering testing
	#Generating an image file output.png with the words that are wrongly rendered
	cmd2 = 'hb-view ' + fontfile + ' --text-file=result.txt > output.png'
	os.system(cmd2)	
	wp.close()
	op.close()
	tp.close()

main()
