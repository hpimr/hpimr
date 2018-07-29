#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import string
import subprocess

import rss

site_name = 'http://xn--c1asif2i.xn--j1amh/'

pages = [
    'help',
    'index',
]
chapters = []
contents = {}

with open('index.asc') as f:
    for line in f:
        match = re.match('^\* link:([0-9]{3}).html\[\{chapter[0-9]{3}\}\] \(([0-9.]+)\)$', line)
        if not match:
            continue

        ch = match.group(1)
        date = match.group(2)

        contents[ch] = {}
        contents[ch] ['date'] = date
        chapters.append(ch)

        # парсимо заголовок розділу із файлу розділу:
        with open(ch + '.asc') as f:
            for line in f:
                match = re.match('^== (.*)', line)
                if match:
                    contents[ch]['title'] = match.group(1)
                    break

def getUrl(ch):
    return '/' + ch + '.html'

def optsForCh(ch):
    return {'url': getUrl(ch), 'title': contents[ch]['title']}

def file_get_contents(filename):
    with open(filename) as f:
        return f.read()

def file_put_contents(filename, data):
    with open(filename, 'w') as f:
        return f.write(data)



templOption = string.Template('<option value="$url">$title</option>')
templPrev = string.Template('<div class="nav-prev"><a href="$url" title="$title" accesskey="p" target="_top">&laquo; Попередній</a></div>')
templNext = string.Template('<div class="nav-next"><a href="$url" title="$title" accesskey="n" target="_top">Наступний &raquo;</a></div>')
templNav = string.Template('<form action="/go.php" method="GET" id="nav-form-top" target="_top">$pr<div class="nav-dropdown"><select name="chapter" class="nav-select">$options</select><noscript><input type="submit" value="Go" /></noscript></div>$ne</form>')
templPage = string.Template(file_get_contents('template.tpl'))
optionsBasic = ''
for ch in chapters:
    optionsBasic += templOption.substitute(optsForCh(ch))

def callAsciidoctor(code, path):
    file_put_contents('tmp.asc', code)
    command = [
        'asciidoctor', '-a', 'lang=uk',
        '-a', 'docinfo1', # додавати в head кожного документа вміст з docinfo.html
        '-a', 'linkcss',
        '-a', 'stylesheet=hpimr.css',
        '-b', 'html5',
        'tmp.asc', '-o', path
    ]
    print(' '.join(command))
    subprocess.call(command)

asciidocVars = ''
for ch in chapters:
    asciidocVars += ':chapter' + ch + ': ' + contents[ch]['title'] + "\n"

for i, ch in enumerate(chapters):
    url = getUrl(ch)
    pr= ''
    ne= ''
    if i != 0:
        pr = templPrev.substitute(optsForCh(chapters[i - 1]))
    if i != len(chapters) - 1:
        ne = templNext.substitute(optsForCh(chapters[i + 1]))
    curOpts = optsForCh(ch)
    options = optionsBasic.replace(getUrl(ch) + '"', getUrl(ch) + '" selected')
    nav = templNav.substitute({'pr': pr, 'ne': ne, 'options': options})
    asciidoc = templPage.substitute({'navi': nav, 'currentChapter': ch, 'vars': asciidocVars})
    callAsciidoctor(asciidoc, 'public_html' + url)

for p in pages:
    asciidoc = templPage.substitute({'navi': '', 'currentChapter': p, 'vars': asciidocVars})
    callAsciidoctor(asciidoc, 'public_html/' + p + '.html')


rss.rss_generate(contents, site_name)

# call sw-precache to generate service worker code
# 'npm install -g sw-precache' should be runned beforehand
subprocess.call([
    'sw-precache',
    '--root=public_html',
    '--config=sw-precache-config.js',
    '--verbose'
])
