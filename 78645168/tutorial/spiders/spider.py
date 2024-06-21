import scrapy
import time
from playwright.async_api import async_playwright


class GoogleJobsSpider(scrapy.Spider):
    name = "google-jobs"
    allowed_domains = ["www.google.com", "consent.google.com"]

    def start_requests(self):
        yield scrapy.Request(
            url="https://www.google.com/search?q=product+designer+nyc&ibp=htl;jobs", callback=self.parse
        )

    async def parse(self, response):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()

            await page.goto(response.url)

            jobs = page.locator("//ul/li")
            num_jobs = await jobs.count()

            for idx in range(num_jobs):
                await jobs.nth(idx).click()

                time.sleep(5)

            await page.context.close()
