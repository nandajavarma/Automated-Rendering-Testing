#!/usr/bin/python
import sys
import os
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
#Defining reference files for font Meera    						
def meera():
	op = open("meera-glyph.txt")
	ff = "Meera.ttf"
	tp = open("hb_meera_rendering.txt") 
	wp = open("ml-test-cases.txt")
	print "The font you have selected is Meera\n"
	return op, tp, wp
#Defining reference files for font Rachana		
def rachana():
	op = open("rachana-glyph.txt")
	ff = "Rachana.ttf"
	tp = open("hb_rachana_rendering.txt")
	wp = open("ml-test-cases.txt")
	print "The font you have selected Rachana\n"
	return op, tp, wp
#Defining reference files for font Suruma
def suruma(): 
	op = open("suruma-glyph.txt")
	ff = "Suruma.ttf"
	tp = open("hb_suruma_rendering.txt")
	wp = open("ml-test-cases.txt")
	print "The font you have selected is Suruma\n"
	return op, tp, wp
#Defining reference files for font Lohit-Malayalam
def lohith(): 
	op = open("lohit-glyph.txt")
	ff = "Lohit-Malayalam.ttf"
	tp = open("hb_lohit_rendering.txt")
	wp = open("ml-test-cases.txt")
	print "The font you have selected is Lohit-Malyalam\n"
	return op, tp, wp
#Leaving an option if the tester want to give the font and the rest of the files herself
def somel():
	wordfile = raw_input("\nEnter the name of the reference words file:")
	reffile  = raw_input("\nEnter its correcponding glyph names' file:")
	rendfile = raw_input("\nEnter the name of the file containing the harfbuzz renderings:")
	op = open(reffile)
	wp = open(wordfile)
	tp = open(rendfile)

ch = int(raw_input("Welcome! Select the font for rendering testing.\n1. Meera\n2. Rachana\n3. Suruma\n4. Lohit-Malayalam\n5. Something else\n"))
choice = {1: meera, 2: rachana, 3: suruma,  4: lohith, 5: somel}

op, tp, wp = choice[ch]()
renderingtest(op, tp, wp)
#Showing the results as the output of hb-view command in output for png
if ch == 1:
	os.system('hb-view Meera.ttf --text-file=result.txt > output.png')
elif ch == 2:
  os.system('hb-view Rachana.ttf --text-file=result.txt > output.png')
elif ch == 3:
  os.system('hb-view Suruma.ttf --text-file=result.txt > output.png')
elif ch == 4:
	os.system('hb-view Lohit-Malayalam.ttf --text-file=result.txt > output.png')

wp.close()
op.close()
tp.close()


