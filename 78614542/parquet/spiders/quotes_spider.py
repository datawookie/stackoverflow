import scrapy

from ..items import ParquetItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
        "https://quotes.toscrape.com/page/2/",
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            item = ParquetItem()

            item["file_urls"] = response.url
            item["text"] = quote.css("span.text::text").get()
            item["author"] = quote.css("small.author::text").get()

            yield item
