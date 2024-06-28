from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time

ACCOUNT_NUMBER = "0523620090003"

URL = "https://hcad.org/property-search/property-search"

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", options=options)

driver.get(URL)

# Change focus to <iframe>.
iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe")))
driver.switch_to.frame(iframe)

# Locate the <input> field.
input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="search"]')))

# Insert search term.
input.send_keys(ACCOUNT_NUMBER)
time.sleep(2)

# Trigger search.
button = driver.find_element(By.CSS_SELECTOR, ".input-group-append button")
button.click()

time.sleep(5)

# Find first search result and click.
row = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr.resulttr.odd")))

row.click()

time.sleep(5)

# Get fiduciary details.
fiduciary = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "i.fa-person-walking-luggage"))
)
details = fiduciary.find_element(By.XPATH, "./../following-sibling::*[1]")
print(details.text)

driver.close()
