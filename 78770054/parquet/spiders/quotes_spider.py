import scrapy


class RugbySpider(scrapy.Spider):
    name = "rugby"
    start_urls = ["https://www.rugbypass.com/live/bristol-vs-leicester/stats/?g=938938"]

    def parse(self, response):
        game_id = response.css("section.game-header::attr('data-id')").get()

        data = []

        for stat in response.css("#statsSummary_stats .stat"):
            data.append(
                {
                    "name": stat.css(".mid::text").get(),
                    "home": stat.css(".line + div::text").get(),
                    "away": stat.css(".mid + div::text").get(),
                }
            )

        yield {"game_id": game_id, "stats": data}
