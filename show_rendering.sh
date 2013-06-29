#!/bin/bash


while read FILE ; do
	count=1
	while read LINE ; do 
		if [ $FILE = $count ]; then
			hb-view $3 $LINE > $LINE.png
		fi
		count=$(($count + 1))
	done < $2

done < $1
	
	
