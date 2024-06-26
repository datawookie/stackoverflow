import requests
from scrapy import Spider, Request
from scrapy_playwright.page import PageMethod

import time

# import time
# from playwright.async_api import async_playwright


# class GoogleJobsSpider(scrapy.Spider):
#     name = "google-jobs"
#     allowed_domains = ["www.google.com", "consent.google.com"]

#     def start_requests(self):
#         yield scrapy.Request(
#             url="https://www.google.com/search?q=product+designer+nyc&ibp=htl;jobs", callback=self.parse
#         )

#     async def parse(self, response):
#         async with async_playwright() as p:
#             browser = await p.chromium.launch(headless=False)
#             page = await browser.new_page()

#             await page.goto(response.url)

#             jobs = page.locator("//ul/li")
#             num_jobs = await jobs.count()

#             for idx in range(num_jobs):
#                 await jobs.nth(idx).click()

#                 time.sleep(5)

#             await page.context.close()


class MySpider(Spider):
    name = "google"

    # def start_requests(self):
    #     url = 'https://www.google.com/search?q=product+designer+nyc&ibp=htl;jobs'
    #     yield Request(
    #         url,
    #         # headers=headers,
    #         meta={
    #             'playwright': True,
    #             'playwright_include_page': True,
    #             # 'errback': self.errback,
    #         }
    #     )

    start_urls = ["https://www.google.com/search?q=product+designer+nyc&ibp=htl;jobs"]

    def start_requests(self):
        consent_url = "https://consent.google.com/save"
        payload = {
            "bl": "boq_identityfrontenduiserver_20240617.06_p0",
            "x": "8",
            "gl": "GB",
            "m": "0",
            "app": "0",
            "pc": "srp",
            "continue": "https://www.google.com/search?q=product+designer+nyc&ibp=htl;jobs",
            "hl": "en",
            "uxe": "none",
            "cm": "2",
            "set_eom": "false",
            "set_sc": "true",
            "set_aps": "true",
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://consent.google.com",
            "Referer": "https://consent.google.com/ml?continue=https://www.google.com/search%3Fq%3Dproduct%2Bdesigner%2Bnyc%26ibp%3Dhtl%3Bjobs&gl=GB&m=0&pc=srp&uxe=none&cm=2&hl=en&src=1",
        }

        # Send the POST request to accept cookies
        response = requests.post(consent_url, data=payload, headers=headers)

        if response.status_code == 200:
            cookies = response.cookies.get_dict()
            cookies_script = f"""
            document.cookie = "{'; '.join([f'{key}={value}' for key, value in cookies.items()])}";
            """

            for url in self.start_urls:
                yield Request(
                    url,
                    meta={
                        "playwright": True,
                        "playwright_include_page": True,
                        "playwright_page_methods": [
                            PageMethod("add_init_script", script=cookies_script),
                            PageMethod("wait_for_selector", "div#search", timeout=10000),
                        ],
                    },
                )
        else:
            self.logger.error("Failed to accept cookies, status code: %d", response.status_code)

        # for url in self.start_urls:
        #     yield Request(
        #         url,
        #         meta={
        #             'playwright': True,
        #             'playwright_include_page': True,
        #             'playwright_page_methods': [
        #                 PageMethod('wait_for_selector', 'input[value="Accept all"]', timeout=5000),
        #                 # PageMethod('click', 'input[value="Accept all"]'),
        #                 # PageMethod('reload'),
        #                 # PageMethod('wait_for_selector', 'div#search', timeout=10000),
        #                 # PageMethod('wait_for_navigation', wait_until='load'),
        #                 # PageMethod('goto', url),  # Navigate back to the original URL
        #                 # PageMethod('wait_for_selector', 'div#search', timeout=10000),
        #             ]
        #         }
        #     )

    #         # .saveButtonContainer > form:nth-child(2) > input:nth-child(14)

    async def parse(self, response):
        page = response.meta["playwright_page"]
        print("YES")
        time.sleep(120)

    #     inp = page.locator('input[value="Accept all"]')
    #     print("XXXXXXXXXXXXXXXXXXXx")
    #     print(inp)
    #     jobs = page.locator("//li")

    #     num_jobs = await jobs.count()

    #     for idx in range(num_jobs):
    #         await jobs.nth(idx).click()
    #         job_details = page.locator("#tl_ditsc")

    #         job_details_html = await job_details.inner_html()
    #         soup = BeautifulSoup(job_details_html, 'html.parser')
    #         data = self.parse_single_jd(soup)

    #         yield {
    #             'idx': idx,
    #             'data': data,
    #         }

    # def parse_single_jd(self, soup):
    #     print("parse_single_jd running!")
    #     title_of_role = soup.h2.text

    #     data = {
    #         "title": title_of_role,
    #     }
    #     return data

    # async def start_requests(self):
    #     for url in self.start_urls:
    #         # Create a Playwright page instance
    #         page = await self.crawler.engine.download(
    #             scrapy.Request(url, meta={'playwright': True, 'playwright_include_page': True}), self
    #         )

    #         # Wait for the cookie consent button and click it
    #         await page.page.wait_for_selector('input[value="Accept all"]', timeout=5000)
    #         await page.page.click('input[value="Accept all"]')

    #         # Wait for the search results to be rendered
    #         await page.page.wait_for_selector('div#search', timeout=10000)

    #         # Get the page content
    #         content = await page.page.content()

    #         # Close the page
    #         await page.page.close()

    #         # Yield the response to the parse method
    #         response = scrapy.http.HtmlResponse(url=url, body=content, encoding='utf-8')
    #         yield self.parse(response)

    # async def parse(self, response):
    #     # Process the content as needed
    #     print(response.text)  # For demonstration, you can parse it with BeautifulSoup or similar tools
    #     # You can continue to extract items as per your scraping logic

    #     # Example: Extract job titles (assuming they are in <h2> tags for demonstration)
    #     for job in response.css('h2::text').getall():
    #         yield {'job_title': job}
