# -*- coding: utf-8 -*-

import requests
from urllib.request import urlopen
from html.parser import HTMLParser

sites = [
    # 'https://www.kinopoisk.ru/',
    # 'https://www.youtube.com/',
    'https://www.urban-university.ru/',
    # 'https://www.ivi.ru/',
    # 'https://ya.ru/',
    # 'https://www.google.ru/?hl=ru',
]


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('Start tag:', tag)
        for attr in attrs:
            print('     attr:', attr)


for url in sites:
    res = urlopen(url)
    html_data = res.read()
    html_data = html_data.decode('utf8')
    total_bytes = len(html_data)
    parser = MyHTMLParser
    parser.feed(html_data)

