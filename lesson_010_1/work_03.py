# -*- coding: utf-8 -*-

import requests
from urllib.request import urlopen
from html.parser import HTMLParser

sites = [
    # 'https://www.kinopoisk.ru/',
    'https://www.fl.ru',
    # 'https://www.youtube.com/',
    # 'https://www.urban-university.ru/',
    # 'https://www.ivi.ru/',
    # 'https://ya.ru/',
    # 'https://www.google.ru/?hl=ru',
]


class LinkExtractor(HTMLParser):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag != 'link':
            return
        # print("Start tag:", tag)
        # for attr in attrs:
        #     print("     attr:", attr)
        attrs = dict(attrs)
        if 'rel' in attrs and attrs['rel'] == 'stylesheet':
            self.links.append(attrs['href'])
        elif tag == 'script':
            if 'src' in attrs:
                self.links.append(attrs['src'])


for url in sites:
    print(f'Go {url}...')
    res = urlopen(url)
    html_data = res.read()
    html_data = html_data.decode('utf8')
    total_bytes = len(html_data)
    extractor = LinkExtractor()
    extractor.feed(html_data)
    print(extractor.links)
    for link in extractor.links:
        print(f'Go {url}...')
        try:
            res = urlopen(link)
        except Exception as exc:
            print(exc)
        extra_data = res.read()
        total_bytes += len(extra_data)
    print(f'For url {url} need download {total_bytes} bytes')
