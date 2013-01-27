#!/bin/bash

# delete dataset directory and tar-ball
rm -rf data-package
rm data-package.tar.gz

# create dataset directory
mkdir data-package
mkdir data-package/json
cp -r images/wl-png data-package/
cp -r images/wl-svg data-package/
cp -r data/json/metadata.json data-package/json
cp -r data/rstat/ data-package/
mv data-package/rstat data-package/csv-rstat
cp doc/licenses/cc-by-nc-at.txt data-package/LICENSE.txt

# create dataset tar-ball
tar czvf data/data-package.tar.gz data-package

# delete dataset directory
rm -rf data-package
