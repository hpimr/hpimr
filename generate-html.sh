#!/bin/bash
set -e

for f in *.asc; do
    echo $f;
    asciidoc $f;
done
mv -v *.html ../public_html
