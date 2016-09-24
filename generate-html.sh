#!/bin/bash
set -e

for f in *.asc; do
    html=${f/asc/html}
    phtml="../public_html/$html"
    if ! [ -e $phtml ] || [ $f -nt $phtml ] ; then
        echo "Updating $f";
        asciidoc -a lang=uk $f;
        mv -v $html ../public_html
    fi
done
