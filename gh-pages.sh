#!/bin/sh
git checkout master
make clean
make html # files are now in build/html/
git checkout gh-pages # build/ is not removed as it is in .gitignore
cp -rf build/html/* current
rm -rf build
