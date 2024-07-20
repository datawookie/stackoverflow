import re
from scrapy import Request
from scrapy.spiders.crawl import CrawlSpider
from scrapy_playwright.page import PageMethod
from twisted.internet.error import TimeoutError

import time

CSS_IMG_LIST = ".MuiStack-root > a > .MuiPaper-root"


class DockerHubSpider(CrawlSpider):
    name = "dockerhub"
    allowed_domains = ["hub.docker.com"]

    def start_requests(self):
        yield Request(
            "https://hub.docker.com/search?q=python&page=1",
            callback=self.parse,
            meta={
                "playwright": True,
                "playwright_include_page": True,
                "playwright_page_methods": [
                    PageMethod("wait_for_selector", CSS_IMG_LIST),
                ],
            },
        )

    async def parse(self, response):
        page = response.meta["playwright_page"]
        time.sleep(5)

        await page.close()

        # Get index for current page.
        index = int(re.search("([0-9]+)$", response.url).groups()[0])

        yield Request(
            f"https://hub.docker.com/search?q=python&page={index+1}",
            callback=self.parse,
            errback=self.handle_error,
            meta={
                "playwright": True,
                "playwright_include_page": True,
                "playwright_page_methods": [
                    PageMethod("wait_for_selector", CSS_IMG_LIST),
                ],
            },
        )

    def handle_error(self, failure):
        if failure.check(TimeoutError):
            raise CloseSpider("TimeoutError encountered")
