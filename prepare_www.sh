#!/bin/bash

if [ ! -d "www/data" ]; then
    mkdir www/data
fi

if [ ! -d "www/images" ]; then
    mkdir www/images
fi

cp data/json/metadata.json www/data/json

cp -r images/wl-png www/images
cp -r images/wl-svg www/images

cp data/data-package.tar.gz www/data
