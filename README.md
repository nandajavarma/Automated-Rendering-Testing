Automated-Rendering-Testing
===========================

GSoC'13 project

This is a framework that can be used to test the correctness of output by rendering engines.

Files required to test using this framework:

1. Test cases file
2. Reference file
3. File with rendering outputs by engines

Create a test cases file that consists all the words that you wish to test the rendering for. Along with this create a reference file that contains the correct glyph names of the words in the test cases file. The framework assumes that the glyph names are in the following format:
[glyph_name1,glyph_name2,glyph_name3,..,glyph_nameN]

Now if the word has more than one correct rendering, provide the next correct one along with this seperated by a semi colon.
For eg: [glyph_name1,glyph_name2,glyph_name3,..,glyph_nameN];[glyph_name1,glyph_name2...,glyph_nameN];..

Now the file with rendering outputs. If the engine you are testing for is Harfbuzz, you need not create this file. The framework considers Harfbuzz as default engine and generate this file automatically. 
If that is not the case, you will have to create it for the font you wish and the rendering of each word must be in the form:
[glyph_name1|glyph_name2|..]

Now that you have all the necessary files, run the script automatedrenderingtesting.py

./automatedrenderingtesting.py

It will ask for the engine of your choice. Then ask for the test cases file, followed by font file and reference file. If you choose harfb
uzz as the engine you need not bother about the rendered outputs' file otherwise you will bee prompted to provide this as well.

Then it will do the comparisons and the ouputs will be stored inside the files you specify. In the case of harfbuzz engine, you will also get the image of the wrong renderings inside the directory you specify.
 
(In the repo I have created samples in four Malayalam fonts. Test cases file being ml-test-cases.txt and reference file being rachana-glyph.txt, suruma-glyph.txt, lohit-glyph.txt and meera-glyph.txt for fonts Rachana, Suruma, Lohit-Malayalam and Meera respectively)


