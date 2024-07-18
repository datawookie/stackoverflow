import scrapy
import json
from urllib.parse import urlencode
import logging

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/json; charset=utf-8",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Referer": "https://www.macmap.org/en//query/results?reporter=826&partner=710&product=010229&level=6",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
}


class ProductSpider(scrapy.Spider):
    name = "product"

    def start_requests(self):
        params = {
            "countryCode": "826",
            "level": "8",
            "code": "010229",
        }

        base_url = "https://www.macmap.org/api/v2/ntlc-products"
        url_with_params = f"{base_url}?{urlencode(params)}"

        yield scrapy.Request(url_with_params, self.parse, headers=headers)

    def parse(self, response):
        records = json.loads(response.text)

        for record in records:
            yield (record)
