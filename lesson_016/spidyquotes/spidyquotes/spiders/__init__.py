# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import json
import scrapy


class SpidyQuoteSpider(scrapy.Spider):
    name = "spidyquotes"
    quotes_base_urls = 'http://spidyquotes.herokuapp.com/api/quotes?page=%s'
    start_urls = [quotes_base_urls % 1]
    download_delay = 1.5

    def parse(self, response):
        data = json.loads(response.body)
        for item in data.get('quotes', []):
            yield {
                'text': item.get('text'),
                'author': item.get('author', {}).get('name'),
                'tags': item.get('tags'),
            }

        if data['has_next']:
            next_page = data['page'] + 1
            yield scrapy.Request(self.quotes_base_urls % next_page)
