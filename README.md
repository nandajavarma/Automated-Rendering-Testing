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
As of now, this will extract the glyphnames from the two files in  order and compare them. So as of now, getting the glyph names in the original glyphs files in correct order as they are given in the words file is a crucial part. 

The script will read both files and compare the corresponding glyph values and writes the line number of the wrongly rendered word appearing in the word file to a new file name result.txt.

The third script show_rendering.sh can be used to see the wrong renderings. It is to be executed as follows:
./show_rendering.sh result.txt wordfile /path/to/fontfile

This will produce png images of the wrongly rendered words in the current folder.

