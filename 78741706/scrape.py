import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = "/usr/bin/chromedriver"

options = Options()

service = Service(executable_path=DRIVER_PATH)

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com/")

time.sleep(5)

html = driver.page_source
print(html)

driver.close()
