from scrapy import Spider, Request


class MySpider(Spider):
    name = "thedogs"

    start_urls = ["https://www.thedogs.com.au/racing/albion-park/2024-05-30/10/tab-flying-amy-classic-h?trial=false"]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, self.parse)

    async def parse(self, response):
        # Get distance once outside of loop.
        distance = response.css(".race-header__info__grade::text").get()

        divs = response.xpath('//tr[@class="accordion__anchor race-runner"]')

        for div in divs:
            yield {
                "distance": distance,
                "grade": div.xpath(".//td[@class='race-runners__grade']/text()").extract(),
                "greyhound": div.xpath("./td[3]/div[1]/a/text()").extract(),
                "position": div.xpath("./td[1]/text()").extract(),
                "trainer": div.xpath(".//div[@class='race-runners__name__trainer']/a/text()").extract(),
                "weight": div.xpath(".//td[@class='race-runners__weight']/text()").extract(),
                "first_sec": div.xpath(".//td[@class='race-runners__sectional']/text()").extract_first(),
                "second_sec": div.xpath(".//td[@class='race-runners__sectional'][2]/text()").extract(),
                "time": div.xpath(".//td[@class='race-runners__time']/text()").extract(),
                "margin": div.xpath(".//td[@class='race-runners__margin']/text()").extract(),
                "starting_price": div.xpath(".//td[@class='race-runners__starting-price']/text()").extract(),
                "date": response.url.split("/")[-3],
                "track": response.url.split("/")[-4],
                "rug": div.xpath('.//td[@class="table__cell--tight race-runners__box"]/sprite-svg/@name').get(),
            }
