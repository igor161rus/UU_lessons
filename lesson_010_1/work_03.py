# -*- coding: utf-8 -*-

import requests
from urllib.request import urlopen
from html.parser import HTMLParser

sites = [
    # 'https://www.kinopoisk.ru/',
    'https://www.fl.ru',
    'https://www.weblancer.net/',
    'https://www.freelancejob.ru/',
    # 'https://kwork.ru',
    'https://work-zilla.com/',
    # 'https://iklife.ru/udalennaya-rabota-i-frilans/poisk-raboty/vse-samye-luchshie-sajty-i-birzhi-v-internete.html',
    # 'https://www.youtube.com/',
    # 'https://www.urban-university.ru/',
    # 'https://www.ivi.ru/',
    # 'https://ya.ru/',
    # 'https://www.google.ru/?hl=ru',
]


class PageSizer:
    def __init__(self, url):
        self.url = url
        self.total_bytes = 0

    def run(self):
        self.total_bytes = 0
        html_data = self._get_html(url=self.url)
        if html_data is None:
            return
        self.total_bytes += len(html_data)
        extractor = LinkExtractor()
        extractor.feed(html_data)
        for link in extractor.links:
            extra_data = self._get_html(url=link)
            if extra_data:
                self.total_bytes += len(extra_data)
        pass

    def _get_html(self, url):
        try:
            res = requests.get(self.url)
        except Exception as exc:
            print(exc)
        else:
            return res.text


class LinkExtractor(HTMLParser):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.links = []

    def handle_starttag(self, tag, attrs):
        # if tag != 'link':
        if tag not in ('link', 'script',):
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
    sizer = PageSizer(url=url)
    sizer.run()
    print(f'For url {url} need download {sizer.total_bytes} bytes')

    # res = requests.get(url)
    # html_data = res.text
    # # html_data = html_data.decode('utf8')
    # total_bytes = len(html_data)
    # extractor = LinkExtractor()
    # extractor.feed(html_data)
    # print(extractor.links)
    # for link in extractor.links:
    #     print(f'Go {url}...')
    #     try:
    #         res = urlopen(link)
    #     except Exception as exc:
    #         print(exc)
    #     # extra_data = res.read()
    #     extra_data = res.text
    #     total_bytes += len(extra_data)
    # print(f'For url {url} need download {total_bytes} bytes')
