Automated Rendering Testing
===========================

A framework to test the correctness of output by rendering engines.

Files required to test rendering using this framework:

(Assuming the user has harfbuzz installed. If not build it from: https://github.com/behdad/harfbuzz)

Files required to test rendering using this framework:

Test cases file Reference file for a specific font File with rendering outputs by engines Font file in ttf format Create a test cases file that consists of all the words that you wish to test the rendering for. Here is a sample test cases file created for Malayalam lamguage: https://github.com/nandajavarma/Automated-Rendering-Testing/blob/master/lohit-ml-test-data/ml-test-cases.txt

Along with this create the reference file that contains the correct glyph names of the words in the test cases file in a particular font. The framework assumes that the glyph names are in the following format: [glyph_name1,glyph_name2,glyph_name3,..,glyph_nameN]

Now if the word has more than one correct rendering, provide the next correct one along with this seperated by a semi colon. For eg: [glyph_name1,glyph_name2,glyph_name3,..,glyph_nameN];[glyph_name1,glyph_name2...,glyph_nameN];.. Here is the reference file for the above mentioned test cases file in the font Rachana: https://github.com/nandajavarma/Automated-Rendering-Testing/blob/master/lohit-ml-test-data/lohit-glyph.txt

Now the file with rendering outputs. If the engine you are testing for is Harfbuzz, you can create this file using the script generate_hb_rendering.py. Run:

./generate_hb_rendering.py -t text_file -f font_file -o output_file 
If that is not the case, you will have to create it for the font you wish and the rendering of each word must be in the form: [glyph_name1|glyph_name2|..] Here is the harfbuzz rendering of the above mentioned test cases file in font Rachana: https://github.com/nandajavarma/Automated-Rendering-Testing/blob/master/lohit-ml-test-data/hb_lohit_ml_rendering.txt

Now that you have all the necessary files, run the script rendering_testing.py with all the file names as parameters.

./rendering_testing.py [-h] [-v] [-w WORD_LIST_FILE] -r REFERENCE_FILE -t
                    RENDERED_OUTPUT_FILE [-o OUTPUT_FILE] [-e ERROR_FILE]
                    [-f FONT_FILE] [-m DIRNAME]
For more info run:

./rendering_testing.py -h 

(In the repo one can find samples in four Malayalam fonts. Test cases file being ml-test-cases.txt and reference file being rachana-glyph.txt, suruma-glyph.txt, lohit-glyph.txt and meera-glyph.txt for fonts Rachana, Suruma, Lohit-Malayalam and Meera respectively)
