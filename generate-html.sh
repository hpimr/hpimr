#!/bin/bash
set -e

for f in *.asc; do
    html="./public_html/${f/asc/html}"
    if ! [ -e $html ] || [ $f -nt $html ] ; then
        echo "Updating $f";
        echo "asciidoc -a lang=uk -a themedir=`pwd`/asciidoc-conf --theme=hpimr -o $html $f";
        asciidoc -a lang=uk -a themedir=`pwd`/asciidoc-conf --theme=hpimr -o $html $f;
    fi
done
