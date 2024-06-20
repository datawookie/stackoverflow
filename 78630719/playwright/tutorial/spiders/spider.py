import scrapy
import time
from bs4 import BeautifulSoup


class CallmeduySpider(scrapy.Spider):
    name = "callmeduy"
    allowed_domains = ["callmeduy.com"]

    def start_requests(self):
        url = "https://callmeduy.com/san-pham"
        yield scrapy.Request(
            url,
            meta=dict(
                playwright=True,
                playwright_include_page=True,
            ),
        )

    async def parse(self, response):
        page = response.meta["playwright_page"]

        while True:
            soup = BeautifulSoup(await page.content(), "lxml")
            wait = soup.select_one(".card-title.h5 > span span.react-loading-skeleton")

            if not wait:
                self.logger.debug("====================================================")
                for card in soup.select(".jss23 .row .col-12"):
                    link = card.select_one("a.jss29")
                    title = card.select_one(".card-title.h5 > span.jss31")

                    self.logger.debug(title.get_text())
                    self.logger.debug(link["href"])

                    # TODO: Probably yield another scrapy.Request() here for each product?
                self.logger.debug("====================================================")

                return
            else:
                self.logger.info("Waiting for skeleton to load.")
                time.sleep(5)
