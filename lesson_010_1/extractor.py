from html.parser import HTMLParser
from urllib.parse import urljoin


class LinkExtractor(HTMLParser):

    def __init__(self, base_url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_url = base_url
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
            link = self._refine(attrs['href'])
            self.links.append(attrs['href'])
        elif tag == 'script':
            if 'src' in attrs:
                self.links.append(attrs['src'])

    def _refine(self, link):
        return urljoin(self.base_url, link)
