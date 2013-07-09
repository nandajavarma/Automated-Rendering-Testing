#!/bin/bash

touch rendered_glyphs.txt
while read ALINE
do
		echo "processing -" $ALINE
		hb-shape $2 $ALINE >> harfbuzz_$2.txt
done < $1 
