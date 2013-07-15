#!/usr/bin/python
import os
import sys
import re

def renderingtest(op, tp):
	rfile = open("result.txt", 'w')
	opfile = op.read()
	tpfile = tp.read()
	olist = []
	tlist = []
	olines = opfile.replace('[','').replace(']','')
	opsop = olines.split('\n')
	for aline in opsop:
		output = aline.split(',')		
		olist.append(output)

	linepart = tpfile.replace('[','').replace(']','') 
	tpsop = linepart.split('\n')
	for line in tpsop:
		newpart = line.split('|')
		tlist.append(newpart)
	m = []
	for x in tlist:
		n = []
		for y in x:
			n.append(y.split('=')[0])
		m.append(n)

	wordfile = wp.read()
	wordlist = []
	wordlist = wordfile.split('\n')
	
	res = []
	res = [i for i, j in zip(olist, m) if i != j]
	if res == []:
		print "No rendering problems found"
		return
	else:
		print "Rendering problems detected for the following words:\n"
		for word in res:	
			d = olist.index(word)
			print wordlist[d]
			rfile.write(wordlist[d] + '\n')
	return rfile
    						
def meera():
	op = open("meera-glyph.txt")
	ff = "Meera.ttf"
	tp = open("harfbuzz_Meera.ttf.txt") 
	print "The font you have selected is Meera"
	return op, tp
	
def rachana():
	op = open("rachana_glyph.txt")
	ff = "Rachana.ttf"
	tp = open("harfbuzz_Rachana.ttf.txt")
	print "The font you have selected Rachana"
	return op, tp

def suruma(): 
	op = open("suruma-glyph.txt")
	ff = "Suruma.ttf"
	tp = open("harfbuzz_Suruma.ttf.txt")
	print "The font you have selected is Suruma"
	return op, tp

def lohith(): 
	op = open("lohith-glyph.txt")
	ff = "Lohit-Malayalam.ttf"
	tp = open("harfbuzz_Lohit-Malayalam.ttf.txt")
	print "The font you have selected is Lohith"
	return op, tp

def somel():
	wordfile = raw_input("\nEnter the name of the reference words file:")
	reffile  = raw_input("\nEnter its correcponding glyph names' file:")
	rendfile = raw_input("\nEnter the name of the file containing the harfbuzz renderings:")
	op = open(reffile)
	tp = open(rendfile)

ch = int(raw_input("Welcome! Select the font for rendering testing.\n1. Meera\n2. Rachana\n3. Suruma\n4. Lohith\n"))
choice = {1: meera, 2: rachana, 3: suruma,  4: lohith, 5: somel}
wp = open("ml-test-cases.txt")

op, tp = choice[ch]()
resultop = renderingtest(op, tp)

if ch == 1:
	os.system("hb-view Meera.ttf --text-file=result.txt >> output.png")
elif ch == 2:
  os.system('hb-view Rachana.ttf --text-file=result.txt >> output.png')
elif ch == 3:
  os.system('hb-view Suruma.ttf --text-file=result.txt >> output.png')
elif ch == 4:
	os.system('hb-view Lohit-Malayalam.ttf --text-file=result.txt >> output.png')




