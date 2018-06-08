#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import sys
import string
import subprocess
from subprocess import CalledProcessError, STDOUT

import smtplib
from email.mime.text import MIMEText

errors_to_mail = []

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
try:
    subprocess.call([
        'sw-precache',
        '--root=public_html',
        '--config=sw-precache-config.js',
        '--verbose'
    ])
    print('sw-precache: success')
except Exception as e:
    print('sw-precache failed: ' + e.message)
    errors_to_mail.append(('sw-precache failed', e.message))

### генерація pdf та epub:
try:
    subprocess.check_output(['./pdf/generate'], stderr=STDOUT)
    print('pdf/generate: success!')
except CalledProcessError as e:
    print('No pdf for you today :(')
    title = 'pdf/generate failed (code %d)' % e.returncode
    errors_to_mail.append((title, e.output))


### відравляємо помилки:
if not errors_to_mail:
    sys.exit()

mail_text = []
for title, text in errors_to_mail:
    mail_text.append('Error: ' + title)
    if text:
        mail_text.extend([
            '=' * 80,
            text,
            '=' * 80
        ])
    mail_text.append('')

### лист із помилками
sender = 'generate@xn--c1asif2i.xn--j1amh'
receiver = '0_0@xn--c1asif2i.xn--j1amh'

# print('\n'.join(mail_text))

msg = MIMEText('\n'.join(mail_text), 'plain', 'utf-8')
msg['Subject'] = 'generate-html.py errors'
msg['From'] = sender
msg['To'] = receiver

smtp = smtplib.SMTP('localhost')
smtp.sendmail(sender, [receiver], msg.as_string())
smtp.quit()
