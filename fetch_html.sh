#!/bin/bash

echo "
*******************************************************************
	          ZAMG CLIMATE DATA HTML DOWNLOAD SCRIPT
*******************************************************************

## ATTENTION ##
This script is just for reproducability purpose, not for execution. 
It downloads the html data from the ZAMG climate data page, which 
is not allowed without permission.

You can find the processed files in the data folder. The data can 
be re-used under Creative Commons by-nc License.

If you want to download the file again, you have to ask for 
permission from the ZAMG (Zentralanstalt für Meteorologie und 
Geodynamik, contact at www.zamg.ac.at).

The programmers do not take any responsibility for unapropiate use 
of this script.

more information:
http://openscience.alpine-geckos.at/projects/zamg-klimadaten/

*******************************************************************
"

exit;

# delete html data directory
if [ -d "data/raw/climate" ]; then
    rm -rf data/raw/climate
fi

# re-create html data directory
mkdir data/raw/climate
cd data/raw/climate
wget -i ../url_climate.txt --force-directories -nH --cut-dirs=6 --wait=0.2
cd ..

# delete the html measures directory
if [ -d "measurments" ]; then
    rm -rf measurements
fi

# re-create measures html directory
mkdir measurements
cd  measurements
wget -i ../url_measurements.txt --force-directories -nH --cut-dirs=6 --wait=0.2
cd ..

LOGFILE=test12.log

q=`/path/to/script.sh`


log(){

     echo "$(date +&#37;c) $*" >>$LOGFILE
}

log "$q"
