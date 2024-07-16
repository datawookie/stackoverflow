import time
from io import StringIO

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://secure.panoramaed.com/ride/understand/1302972/survey_results/27746568#/questions"
URL_AUTH = "https://secure.panoramaed.com/ride/understand?auth_token=geZrUH8yRr8_Ln_C9LH3"

DRIVER_PATH = "/usr/bin/chromedriver"

options = Options()

service = Service(executable_path=DRIVER_PATH)

driver = webdriver.Chrome(service=service, options=options)

# Authenticate.
driver.get(URL_AUTH)
# Open target page.
driver.get(URL)

time.sleep(5)

questions = driver.find_elements(By.CSS_SELECTOR, ".expandable-row")

for question in questions:
    # Open question.
    driver.execute_script("arguments[0].click();", question)
    time.sleep(3)

    # Open context menus.
    menus = driver.find_elements(By.XPATH, "//button[@aria-label='View chart menu, Chart']")

    for menu in menus:
        driver.execute_script("arguments[0].click();", menu)
        time.sleep(1)
    
    # Get buttons to display tables.
    views = driver.find_elements(By.XPATH, "//li[contains(text(), 'View data table')]")

    for view in views:
        driver.execute_script("arguments[0].click();", view)
        time.sleep(1)

    # Now scrape the contents of the revealed tables.
    #
    tables = driver.find_elements(By.CSS_SELECTOR, ".highcharts-data-table > table")
    for table in tables:
        df = pd.read_html(StringIO(table.get_attribute("outerHTML")))[0]
        print(df)

    # Close question.
    driver.execute_script("arguments[0].click();", question)
    time.sleep(3)

driver.close()
