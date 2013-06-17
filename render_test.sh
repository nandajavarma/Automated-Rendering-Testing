#!/bin/bash

touch rendered_glyphs.txt
while read ALINE
do
		echo "processing -" $ALINE
		hb-shape /usr/share/fonts/truetype/malayalam-fonts/Meera.ttf $ALINE >>rendered_glyphs.txt
done < $1
