#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

rss_start = '''<?xml version="1.0" encoding="UTF-8" ?>
<rss xmlns:atom="http://www.w3.org/2005/Atom" version="2.0">
  <channel>
    <title>
      Гаррі Поттер і Методи Раціональності
    </title>
    <link>%s</link>
    <atom:link href="http://hpmor.com/rss.xml" rel="self" type="application/rss+xml"/>
    <description>
        Український переклад чудового фанфіку Harry Potter and the methods of rationality, від Eliezer Yudkowsky
    </description>
    <language>uk-ua</language>
    <pubDate>%s</pubDate>
    <generator>Генератор rss для гпімр.укр від Qgelena</generator>
    <webMaster>0_0@гпімр.укр</webMaster>
'''

rss_item_templ = ''' 
    <item>
      <title>%s</title>
      <link>%s</link>
      <description>%s</description>
      <pubDate>%s</pubDate>
    </item>
'''

rss_end = '''  </channel>
</rss>
'''
 

def rss_generate(data, site_name): 
    '''
    функція приймає дані в форматі: 
    {
    '001': {'title': 'Розділ 1. День вкрай низької ймовірності', 'date': '22.09.2016'},
    '002': {'title': 'Розділ 2. Все, у що я вірю, — хибне', 'date': '24.09.2016'},
    '003': {'title': 'Розділ 3. Порівнюючи реальність з її альтернативами', 'date': '26.09.2016'},
    }
    ключ — номер розділу, значення — словник з title і date;
    функція записує згенеровану rss-стрічку в public_html/rss.xml
    ''' 
    # itemlist зберігає оновлення в порядку від новіших до старіших; 
    itemlist = [] 
    for chapter, info in data.items():
        day, month, year = info['date'].split('.')
        d = datetime.date(int(year), int(month), int(day))
        itemlist.append((d, chapter))

    # сортуємо по даті в зворотному порядку;
    itemlist.sort(reverse=True)

    with open('public_html/rss.xml', 'w') as f:
        pub_date = itemlist[0][0].strftime('%a, %d %b %Y 00:00:00 +0300')
        f.write(rss_start % (site_name, pub_date))

        for d, chapter in itemlist:
            info = data[chapter]

            title = info['title']
            link = site_name + chapter + '.html'
            desc = title + '--' + info['date']

            date = d.strftime('%a, %d %b %Y 00:00:00 +0300')
            f.write(rss_item_templ % (title, link, desc, date))
        f.write(rss_end)

