import logging

from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule

# from scrapy.spiders.crawl import CrawlSpider, Rule
from scrapy_playwright.page import PageMethod
from scrapy.linkextractors import LinkExtractor

logging.getLogger("scrapy-playwright").setLevel(logging.WARNING)
logging.getLogger("playwright").setLevel(logging.WARNING)


# class DockerhubDockerRegistrySpider(CrawlSpider):
#     name = "dockerhub"
#     allowed_domains = ["hub.docker.com"]

#     def start_requests(self):
#         url = "https://hub.docker.com/search?q=python"
#         yield Request(
#             url,
#             callback=self.parse,
#             meta=dict(
#                 playwright=True,
#                 playwright_include_page=True,
#                 playwright_page_methods=[
#                     PageMethod("wait_for_selector", "#searchResults .MuiStack-root > a.MuiLink-root", state="visible"),
#                     #     PageMethod('pause')
#                 ],
#             ),
#         )

#     async def parse(self, response):
#         page = response.meta["playwright_page"]

#         links = response.css("#searchResults .MuiStack-root > a.MuiLink-root::attr(href)").getall()

#         for link in links:
#             link = response.urljoin(link)

#             yield Request(
#                 link,
#                 callback=self.parse_image,
#                 meta=dict(
#                     playwright=True,
#                     playwright_include_page=True,
#                     playwright_page_methods=[
#                         PageMethod("wait_for_selector", ".MuiTypography-root.MuiTypography-h2", state="visible"),
#                         #     PageMethod('pause')
#                     ],
#                 ),
#             )

#         await page.close()

#     async def parse_image(self, response):
#         page = response.meta["playwright_page"]

#         title = response.css(".MuiTypography-root.MuiTypography-h2::text").get()

#         await page.close()

#         yield {"title": title}


class DockerhubDockerRegistrySpider(CrawlSpider):
    name = "dockerhubDockerQueriedRegistrySearchSpiderTemp"
    allowed_domains = ["hub.docker.com"]

    rules = (
        Rule(
            LinkExtractor(allow=r"/tags$"),  # Only allow URLs that end with '/tags'
            callback="parse_additional_page",
            follow=False,
        ),
        Rule(LinkExtractor(allow="search"), callback="parse_registry", follow=True),
    )

    def __init__(self, query=None, *args, **kwargs):
        super(DockerhubDockerRegistrySpider, self).__init__(*args, **kwargs)
        self.query = query
        self.start_urls = [f"https://hub.docker.com/search?q={query}&page={i}" for i in range(1, 12)]

    def start_requests(self):
        for index, url in enumerate(self.start_urls, start=1):
            self.logger.info(f"Starting request: {url}")
            yield Request(
                url,
                meta=dict(
                    page_number=index,
                    playwright=True,
                    playwright_include_page=True,
                    playwright_page_methods={
                        "wait_for_search_results": PageMethod("wait_for_selector", "div#searchResults"),
                    },
                ),
                callback=self.parse_registry,
            )

    async def parse_registry(self, response):
        page = response.meta["playwright_page"]

        # if await page.title() == "hub.docker.com":
        await page.close()
        await page.context.close()

        # page_number = response.meta.get("page_number")
        # if page_number is None:
        #     self.logger.warning("Page number not found in meta: %s", response.url)
        #     return

        search_results = response.xpath('//a[@data-testid="imageSearchResult"]')

        for result in search_results:
            #     # item = {}
            #     # item['page_number'] = page_number
            #     # item['name'] = result.css('[data-testid="product-title"]::text').get()

            #     # uploader_elem = result.css("span::text").re(r"^By (.+)")

            #     # if uploader_elem:
            #     #     item["uploader"] = uploader_elem[0].strip()
            #     # else:
            #     #     official_icon = result.css('[data-testid="official-icon"]')
            #     #     verified_publisher_icon = result.css(
            #     #         '[data-testid="verified_publisher-icon"]'
            #     #     )

            #     #     item["is_official_image"] = bool(official_icon)
            #     #     item["is_verified_publisher"] = bool(verified_publisher_icon)

            #     # item['is_official_image'] = bool(result.css('[data-testid="official-icon"]'))
            #     # item['is_verified_publisher'] = bool(result.css('[data-testid="verified_publisher-icon"]'))
            #     # item['last_update'] = self.parse_update_string(result.css('span:contains("Updated")::text').get())

            #     # item['description'] = result.xpath(
            #     #     './/span[contains(text(), "Updated")]/ancestor::div[1]/following-sibling::p[1]/text()').get()

            #     # item['chips'] = result.css('[data-testid="productChip"] span::text').getall()

            #     # # Extract pulls last week
            #     # pulls_elem = (
            #     #     result.css('p:contains("Pulls:")')
            #     #     .xpath("following-sibling::p/text()")
            #     #     .get()
            #     # )
            #     # item["pulls_last_week"] = (
            #     #     pulls_elem.replace(",", "") if pulls_elem else None
            #     # )

            #     # item['downloads'] = result.css('[data-testid="DownloadIcon"] + p::text').get()
            #     # item['stars'] = result.css('svg[data-testid="StarOutlineIcon"] + span > strong::text').get()

            #     # # Clean up text fields
            #     # item['name'] = item['name'].strip() if item['name'] else None
            #     # item['description'] = item['description'].strip() if item['description'] else None
            #     # item['downloads'] = item['downloads'].strip() if item['downloads'] else None
            #     # item['pulls_last_week'] = item['pulls_last_week'].replace(",", "") if item['pulls_last_week'] else None
            #     # item['stars'] = item['stars'].strip() if item['stars'] else None

            additional_data_url = result.attrib.get("href")
            if additional_data_url and "/r/" or "/_/" in additional_data_url and "/tags" in additional_data_url:
                additional_data_url_absolute = f"https://hub.docker.com{additional_data_url}/tags"
                self.logger.info("Entered Additional Page: %s", additional_data_url_absolute)

                # yield Request(
                #     additional_data_url_absolute,
                #     meta=dict(
                #         # page_number=index,
                #         playwright=True,
                #         playwright_include_page=True,
                #         # playwright_page_methods={
                #         #     "wait_for_search_results": PageMethod("wait_for_selector", "div#searchResults"),
                #         # }
                #     ),
                #     callback=self.parse_registry
                # )
                yield Request(
                    additional_data_url_absolute,
                    callback=self.parse_additional_page,
                    meta=dict(
                        playwright=True,
                        playwright_include_page=True,
                        # playwright_page_methods=[
                        #     PageMethod("wait_for_selector", ".MuiTypography-root.MuiTypography-h2", state="visible"),
                        #     #     PageMethod('pause')
                        # ],
                    ),
                )

                # yield response.follow(
                #     additional_data_url_absolute,
                #     callback=self.parse_additional_page,
                #     # cb_kwargs=dict(item=item),
                #     meta=dict(
                #         playwright=True,
                #         playwright_include_page=True,
                #         errback=self.close_context_on_error,
                #         playwright_page_methods={
                #             "wait_for_page_load": PageMethod("wait_for_selector", 'div[data-testid="repotagsTagListItem"]'),
                #         },
                #         playwright_context_kwargs={
                #             "ignore_https_errors": True,
                #         }
                #     )
                # )
            # else:
            #     self.logger.error("No additional page available for: %s", item['name'])
            #     yield item

    async def close_context_on_error(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
        await page.context.close()

    async def parse_additional_page(self, response, item):
        page = response.meta["playwright_page"]

        # if await page.title() == "hub.docker.com":
        await page.close()
        await page.context.close()

        # self.logger.info("Additional page meta: %s", response.meta)
        # self.logger.info("Additional page HTML: %s", response.css('title::text').get())
        # self.logger.info("Additional page HTML Repo-Name: %s", response.css('h2[data-testid="repoName"]::text').get())
        # item['additional_data'] = response.css('h2[data-testid="repoName"]::text').get()
        # return item

    @staticmethod
    def parse_update_string(update_string):
        return update_string.strip() if update_string else None
