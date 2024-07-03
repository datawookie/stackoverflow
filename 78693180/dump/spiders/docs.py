import scrapy
from bs4 import BeautifulSoup


class DevgrossSpider(scrapy.Spider):
    name = "devgross"
    allowed_domains = ["devgrossonline.com"]
    start_urls = [
        "https://devgrossonline.com/sut-kahvaltilik",
        "https://devgrossonline.com/meyve-sebze",
        "https://devgrossonline.com/et-sarkuteri",
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                meta=dict(
                    playwright=True,
                    playwright_include_page=True,
                ),
            )

    async def parse(self, response):
        page = response.meta["playwright_page"]

        await page.wait_for_selector("ul.pagination")

        html = await page.content()
        soup = BeautifulSoup(html, "html.parser")

        await page.close()

        products = soup.select("div.urun-kutusu")

        for product in products:
            name = product.select_one("h2 a").string.strip()
            price = product.select_one("div.urun-fiyat span").string.strip()

            yield {
                "name": name,
                "price": price,
            }
