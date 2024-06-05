import scrapy
from bs4 import BeautifulSoup
from urllib.parse import urlparse


class DocsSpider(scrapy.Spider):
    name = "docs"
    allowed_domains = ["disneycruise.disney.go.com"]

    def start_requests(self):
        url = "https://disneycruise.disney.go.com/cruises-destinations/list/"
        yield scrapy.Request(
            url,
            meta=dict(
                playwright=True,
                playwright_include_page=True,
            ),
        )

    async def parse(self, response):
        page = response.meta["playwright_page"]

        await page.wait_for_selector("product-availability-root")

        await page.wait_for_function(
            """
            () => {
                const element = document.querySelector("product-availability-root");
                return element && element.innerHTML.trim().length > 0;
            }
            """
        )

        await page.wait_for_selector('.product-card-list', timeout=30000)

        html = await page.content()

        await page.close()

        soup = BeautifulSoup(html, 'html.parser')

        for title in soup.find_all('h2', class_="product-card-content__name"):
            print(title.get_text())