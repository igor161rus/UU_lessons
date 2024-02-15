# -*- coding: utf-8 -*-
import requests
import threading
from extractor import LinkExtractor
from utils import time_track

sites = [
    # 'https://www.kinopoisk.ru/',
    'https://www.fl.ru',
    'https://www.weblancer.net/',
    'https://www.freelancejob.ru/',
    'https://kwork.ru',
    'https://work-zilla.com/',
    # 'https://iklife.ru/udalennaya-rabota-i-frilans/poisk-raboty/vse-samye-luchshie-sajty-i-birzhi-v-internete.html',
    # 'https://www.youtube.com/',
    # 'https://www.urban-university.ru/',
    # 'https://www.ivi.ru/',
    # 'https://ya.ru/',
    # 'https://www.google.ru/?hl=ru',
]


class PageSizer(threading.Thread):
    def __init__(self, url, go_ahead=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url
        self.go_ahead = go_ahead
        self.total_bytes = 0

    def run(self):
        self.total_bytes = 0
        html_data = self._get_html(url=self.url)
        if html_data is None:
            return
        self.total_bytes += len(html_data)
        if self.go_ahead:
            extractor = LinkExtractor(base_url=self.url)
            extractor.feed(html_data)
            sizers = [PageSizer(url=link, go_ahead=False) for link in extractor.links]
            for sizer in sizers:
                sizer.start()
            for sizer in sizers:
                sizer.join()
            for sizer in sizers:
                self.total_bytes += sizer.total_bytes


    def _get_html(self, url):
        try:
            print(f'Go {url}...')
            res = requests.get(self.url)
        except Exception as exc:
            print(exc)
        else:
            return res.text


@time_track
def main():
    sizers = [PageSizer(url=url) for url in sites]

    for sizer in sizers:
        # sizer.run()
        sizer.start()
    for sizer in sizers:
        sizer.join()
    for url in sites:
        print(f'For url {url} need download {sizer.total_bytes // 1024} Kb ({sizer.total_bytes} bytes)')


if __name__ == '__main__':
    main()
# for url in sites:
#     print(f'Go {url}...')
#     sizer = PageSizer(url=url)
#     sizer.run()
#     print(f'For url {url} need download {sizer.total_bytes} bytes')

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
