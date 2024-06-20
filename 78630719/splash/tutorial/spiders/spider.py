import base64
from pathlib import Path

import scrapy
from scrapy_splash import SplashRequest


class CallmeduySpider(scrapy.Spider):
    name = "callmeduy"

    script = """
    function main(splash, args)
        splash:go(args.url)
        splash:wait(5)  -- Initial wait time
        local max_wait_time = 20  -- Max wait time in seconds
        local wait_time = 0
        while not splash:select('div.container-fluid') and wait_time < max_wait_time do
            splash:wait(1)
            wait_time = wait_time + 1
        end
        return {
            html = splash:html(),
            png = splash:png(),  -- Capture screenshot for debugging
            har = splash:har(),
        }
    end
    """

    def start_requests(self):
        urls = ["https://callmeduy.com/san-pham/"]
        for url in urls:
            yield SplashRequest(
                url=url,
                callback=self.parse,
                endpoint="execute",
                args={
                    "wait": 10,
                    "timeout": 90,
                    "images": 0,
                    "lua_source": self.script,
                },
            )

    def parse(self, response):
        print(response.body)
        f = open("res.html", "w+")
        f.write(str(response.body))
        f.close()

        print(response.data["png"])

        # with open('res.png', 'wb') as f:
        #     f.write(response.data['png'])
        # with open('res.har', 'w') as f:
        #     f.write(response.data['har'])

        with open("res.png", "wb") as f:
            f.write(base64.b64decode(response.data["png"]))
