#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import re
import string
import subprocess

pages = [
    'help',
    'index',
]
chapters = []

with open('index.asc') as f:
    for line in f:
        match = re.match('^\* link:([0-9]{3}).html\[\{chapter[0-9]{3}\}\] \([0-9.]+\)$', line)
        if match:
            ch = match.group(1)
            chapters.extend([ch,])

def getUrl(ch):
    return '/' + ch + '.html'

def optsForCh(ch):
    return {'url': getUrl(ch), 'title': contents[ch]['title']}

contents = {}
for num in chapters:
    p = getUrl(num)
    contents[num] = {
        'title': '',
    }
    with open(num + '.asc') as f:
        for line in f:
            match = re.match('^== (.*)', line)
            if match:
                contents[num]['title'] = match.group(1)
                break

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


def get_last_change_timestamp(filename):
    git_output = subprocess.check_output([
        'git', 'log', '-1', '--date=raw', filename
    ])
    return int(re.findall(r'Date:\s+(\d+)', git_output)[0])

def create_service_worker():
    index_ts = get_last_change_timestamp('index.asc')
    files2cache = {
        '/': index_ts
    }
    for fn in [
        'fleur.png',
        'icon192.png',
        'hpimr.css',
        'jquery-ui.css',
        'manifest.json',
        'script.js',
    ]:
        files2cache[fn] = get_last_change_timestamp('public_html/' + fn)

    for p in pages:
        files2cache[p + '.html'] = max(get_last_change_timestamp(p + '.asc'), index_ts)

    for c in chapters:
        files2cache[c + '.html'] = get_last_change_timestamp(c + '.asc')

    template = file_get_contents('sw.template.js')
    sw = template.replace(
        '__FILES_TO_CACHE__',
        json.dumps(files2cache, indent=4)
    )
    print('public_html/sw.js')
    file_put_contents('public_html/sw.js', sw)

create_service_worker()
