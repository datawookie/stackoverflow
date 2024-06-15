import scrapy
import pandas as pd
from io import StringIO


class QuotesSpider(scrapy.Spider):
    name = "parquet"
    start_urls = ["https://onlinetestcase.com/csv-file/"]

    def parse(self, response):
        for url in response.css("a::attr(href)").extract():
            if url.endswith(".csv"):
                url = response.urljoin(url)

                yield scrapy.http.Request(url, callback=self.parse_csv, dont_filter=True)

    def parse_csv(self, response):
        yield {
            "url": response.url,
            # Convert CSV text into Data Frame.
            "data": pd.read_csv(StringIO(response.text)),
        }
