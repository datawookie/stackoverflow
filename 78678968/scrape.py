import time
from io import StringIO

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd


playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False, slow_mo=2000)
context = browser.new_context(
    viewport={"width": 1280, "height": 900}
)

page = context.new_page()

tables = []

for i in range(1, 4):
    URL = f"https://www.coingecko.com/?page={i}"
    print(f"URL: {URL}")

    page.goto(URL)

    time.sleep(5)

    html = page.content()

    table = pd.read_html(StringIO(html))[0]
    tables.append(table)

page.close()

data = pd.concat(tables)

data = data.loc[:, data.columns[1:-1]]

data.to_csv('crypto-data.csv', index=False)
