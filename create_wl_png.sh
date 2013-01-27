#!/bin/bash

if [ -d "images/wl-svg" ]; then
    rm -rf images/wl-svg
fi

mkdir images/wl-svg
mv data/r/*.svg images/wl-svg

FILES=`ls images/wl-svg/*svg`

for FILE in $FILES
do
	# add copyright text
    sed -i -e 's/<\/svg>/<text x="460" y="490" text-anchor="end" style="font-family: Arial; font-size: 9pt;" >Copyright: Creative Commons by-nc, Quelle: ZAMG www.zamg.ac.at<\/text><\/svg>/g' $FILE
	# create png out of the svg
    convert $FILE -resize 360x360 ${FILE%.svg}_small.png
    convert $FILE -resize 600x600 ${FILE%.svg}_big.png
done

# delete png data directory
if [ -d "images/wl-png" ]; then
    rm -rf images/wl-png
fi

mkdir images/wl-png
mv images/wl-svg/*png images/wl-png

