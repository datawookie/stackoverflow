from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class WikiSpider(CrawlSpider):
    name = "wiki"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Main_Page"]

    seen = set()

    rules = (Rule(LinkExtractor(), callback="parse_url", follow=False),)

    def parse_url(self, response):
        if response.url not in self.seen:
            self.seen.add(response.url)
            yield {"url": response.url}
