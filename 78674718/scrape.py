import time
from io import StringIO

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd

# 🚨 Specific URL for getting Bitcoin markets.
#
URL = f"https://www.coingecko.com/en/coins/1/markets/spot"

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, slow_mo=2000)
context = browser.new_context(viewport={"width": 1280, "height": 900})

page = context.new_page()


def fetch_page(url):
    print(url)
    page.goto(url)
    time.sleep(5)

    return page.content()


def scrape_all_pages(url, max_pages=10):
    markets = []
    for page in range(1, max_pages + 1):
        html = fetch_page(f"{url}?page={page}")

        df = pd.read_html(StringIO(html))
        markets.extend(df)

    return pd.concat(markets, ignore_index=True)


max_pages = 10
df = scrape_all_pages(URL, max_pages)

page.close()

df = df.dropna(how="all")

print(df)
