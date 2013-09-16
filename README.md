Automated Rendering Testing
===========================

A framework to test the correctness of output by rendering engines.

Files required to test rendering using this framework:

(Assuming the user has harfbuzz installed. If not build it from: https://github.com/behdad/harfbuzz)

Files required to test rendering using this framework:

Test cases file Reference file for a specific font File with rendering outputs by engines Font file in ttf format Create a test cases file that consists of all the words that you wish to test the rendering for. Here is a sample test cases file created for Malayalam lamguage: https://github.com/nandajavarma/Automated-Rendering-Testing/blob/master/ml-test-data/ml-test-cases.txt

Along with this create the reference file that contains the correct glyph names of the words in the test cases file in a particular font. The framework assumes that the glyph names are in the following format: [glyph_name1,glyph_name2,glyph_name3,..,glyph_nameN]

Now if the word has more than one correct rendering, provide the next correct one along with this seperated by a semi colon. For eg: [glyph_name1,glyph_name2,glyph_name3,..,glyph_nameN];[glyph_name1,glyph_name2...,glyph_nameN];.. Here is the reference file for the above mentioned test cases file in the font Rachana: https://github.com/nandajavarma/Automated-Rendering-Testing/blob/master/ml-test-data/lohit-ml-test-data/lohit-glyph.txt

Now the file with rendering outputs. If the engine you are testing for is Harfbuzz, you can create this file using the following command:

	cat ml-test-data.txt | hb-shape /path/to/Font.ttf > output.txt

If that is not the case, you will have to create it for the font you wish and the rendering of each word must be in the form: [glyph_name1|glyph_name2|..] Here is the harfbuzz rendering of the above mentioned test cases file in font Rachana: https://github.com/nandajavarma/Automated-Rendering-Testing/blob/master/ml-test-data/lohit-ml-test-data/hb_lohit_rendering.txt

Now that you have all the necessary files, write these data to an .ini file for the main script to read. Here is the structure:
	[main]
    Reference-file: 
    Rendered-output: 
    Font-file: 
    Test-cases-file: 
    Output-file: 
    Directory-name: 
Out of these, Reference-file and Rendered-output are mandatory. Comment out all the other lines, if a result file is not necessary. A directory-name is to be provided if the shaping engine to be tested is harfbuzz. It is to store the rendered images by harfbuzz. Here is a sample: 

Now to test, run the script rendering_test.py passing the name of the .ini file as a parameter.
For example:
	./rendering_test.py Meera.ini

(In the repo one can find samples in four Malayalam fonts and one Devanagari font. Test cases file for Malayalam being  and for Devanagari being.The rerence files are   for the fonts Rachana, Suruma, Lohit-Malayalam, Meera and Lohit-Devanagari respectively)
