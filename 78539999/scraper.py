from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    options=webdriver.ChromeOptions(),
)
driver.maximize_window()
driver.implicitly_wait(10)

URL = "https://www.nepsealpha.com/nepse-data"
driver.get(URL)

time.sleep(5)

date_start = driver.find_element(By.CSS_SELECTOR, "input[min='2019-05-28']")

print(date_start)

date_start.send_keys("01/01/2020")
date_start.send_keys(Keys.ENTER)

date_end = driver.find_element(By.CSS_SELECTOR, "input[max='2024-05-28']:not([min])")

print(date_end)

date_end.send_keys("01/01/2021")
date_end.send_keys(Keys.ENTER)

time.sleep(10)

driver.quit()
