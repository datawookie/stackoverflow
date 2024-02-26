import time
from playwright.sync_api import sync_playwright, TimeoutError

with sync_playwright() as p:
    browser = p.firefox.launch(headless=True)

    context = browser.new_context(viewport={"width": 1280, "height": 900})
    page = context.new_page()

    page.goto("https://www.python.org/")
    time.sleep(10)
