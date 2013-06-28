Automated-Rendering-Testing
===========================

GSoC'13 project

The first thing to be done is select a set of charaters/words for the language and run it through the render_test.sh script as follows:
		./render_test.sh /path/to/wordfile /path/to/fontfile

This will yield a rendered_glyphs.txt file which will contain the harfbuzz hb-shape output of the words along which basically gives the glyph name along with some other data as its output. 

Now create a file with correct glyph names of the words specified in the first file. That too in the same order as in the word file and alsoof the form:
		[glyphname1,glyphname2,glyphname3,....glyphnameN]

Now run the above two files through the main script rendering_testing.c, i.e. after executing and getting the executable file a.out, run:
		./a.out orig_glyph.txt rendered_glyphs.txt
As of now, this will extract the glyphnames from the two files in  order and compare them. So as of now, getting the glyph names in the original glyphs files in correct order as they are given in the words file is a crucial part. Further steps would be to get the wrong ones into another file on which we can execute a fourth bash script and get its hb-shape output and also to make the code efficient.

