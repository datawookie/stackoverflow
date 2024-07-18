import scrapy


class ParquetItem(scrapy.Item):
    file_urls = scrapy.Field()
    text = scrapy.Field()
    author = scrapy.Field()
