#!/bin/bash
set -e;
export PREFIX=~/opt
mkdir -vp $PREFIX;
mkdir -vp ~/build;

cd ~/build;
wget -c http://ftp.gnu.org/gnu/gettext/gettext-0.19.8.tar.gz;
tar -xvf gettext-0.19.8.tar.gz;
cd gettext-0.19.8.tar.gz;
./configure --prefix=$PREFIX --disable-static;
make;
make install;

cd ~/build;
ver=2.15.1
wget -c https://www.kernel.org/pub/software/scm/git/git-$ver.tar.gz;
tar -xvf git-$ver.tar.gz;
cd git-$ver;
./configure --prefix=$PREFIX;
make;
make install;

cd ~/build;
wget -c http://ftp.ruby-lang.org/pub/ruby/ruby-2.3.3.tar.bz2;
tar -xvf ruby-2.3.3.tar.bz2;
cd ruby-2.3.3;
./configure --prefix=$PREFIX --enable-shared --disable-install-doc;
make;
make install;

# install asciidoctor
gem install asciidoctor
NOKOGIRI_USE_SYSTEM_LIBRARIES=1 gem install asciidoctor-epub3 --pre
# small patch for html5 quotes:
f=$(find $PREFIX -name "html5.rb")
sed -i -e "s/'&#8220;',  '&#8221;',   false/'{ldquo}',  '{rdquo}',   false/" \
       -e "s/'&#8216;',  '&#8217;',   false/'{lsquo}',  '{rsquo}',   false/" $f

# install node (npm, node.js)
#ver=6.11.0
ver=8.1.3
cd ~/build;
wget -c https://nodejs.org/dist/v$ver/node-v$ver.tar.gz
tar -xvf node-v$ver.tar.gz
cd node-v$ver/
./configure --prefix=$PREFIX
make
make install

#install sw-precache
npm install -g sw-precache

#install asciidoctor-pdf
gem install asciidoctor-pdf --pre
