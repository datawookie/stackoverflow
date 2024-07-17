import logging

from scrapy import Request
from scrapy.spiders import CrawlSpider
from scrapy_playwright.page import PageMethod

logging.getLogger("scrapy-playwright").setLevel(logging.WARNING)
logging.getLogger("playwright").setLevel(logging.WARNING)


class DockerhubDockerRegistrySpider(CrawlSpider):
    name = "dockerhub"
    allowed_domains = ["hub.docker.com"]

    def start_requests(self):
        url = "https://hub.docker.com/search?q=python"
        yield Request(
            url,
            callback=self.parse,
            meta=dict(
                playwright=True,
                playwright_include_page=True,
                playwright_page_methods=[
                    PageMethod("wait_for_selector", "#searchResults .MuiStack-root > a.MuiLink-root", state="visible"),
                    #     PageMethod('pause')
                ],
            ),
        )

    async def parse(self, response):
        page = response.meta["playwright_page"]

        links = response.css("#searchResults .MuiStack-root > a.MuiLink-root::attr(href)").getall()

        for link in links:
            link = response.urljoin(link)

            yield Request(
                link,
                callback=self.parse_image,
                meta=dict(
                    playwright=True,
                    playwright_include_page=True,
                    playwright_page_methods=[
                        PageMethod("wait_for_selector", ".MuiTypography-root.MuiTypography-h2", state="visible"),
                        #     PageMethod('pause')
                    ],
                ),
            )

        await page.close()

    async def parse_image(self, response):
        page = response.meta["playwright_page"]

        title = response.css(".MuiTypography-root.MuiTypography-h2::text").get()

        await page.close()

        yield {"title": title}
