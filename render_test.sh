#!/bin/bash

touch rendered_glyphs.txt
while read ALINE
do
		echo "processing -" $ALINE
		hb-shape $2 $ALINE >> rendered_glyphs.txt
done < $1 
