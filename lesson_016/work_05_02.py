import json
import scrapy


# scrapy startproject spidyquotes
# Положить код в папку spidyquotes\spiders\__init__.py
# cd spidyquotes/
# scrapy crawl spidyquotes

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
