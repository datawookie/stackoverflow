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
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

driver = webdriver.Remote(
  "http://127.0.0.1:4444/wd/hub",
  options=options
)

driver.get(URL)

time.sleep(2)

iframe = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe'))
)
driver.switch_to.frame(iframe)

input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="search"]'))
)

# input.click()

input.send_keys(ACCOUNT_NUMBER)

time.sleep(2)

button = driver.find_element(By.CSS_SELECTOR, '.input-group-append button')
print(button)
button.click()

time.sleep(5)

print(input)
# print(link.text)

row = driver.find_element(By.CSS_SELECTOR, 'tr.resulttr.odd')
print(row)

row.click()

time.sleep(5)

driver.close()

# body > div.container-fluid > main > div > div.container-md > div > div.col-md-10 > div > div > input

# /html/body/div[1]/main/div/div[1]/div/div[1]/div/div/input