from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from dotenv import load_dotenv
load_dotenv()

import os

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

options = Options()

driver = webdriver.Remote(
    "http://127.0.0.1:4444/wd/hub",
    DesiredCapabilities.CHROME,
    options=options
)

driver.get("https://twitter.com/login")

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[autocomplete='username']"))
)

username.send_keys(USERNAME)

time.sleep(5)

driver.find_element(By.XPATH, "//button[@type='button' and .//span[text()='Next']]").click()

time.sleep(5)

password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[autocomplete='current-password']"))
)

password.send_keys(PASSWORD)

print("AGAIN")

password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[autocomplete='current-password']"))
)

password.send_keys(PASSWORD)

driver.find_element(By.XPATH, "//button[@data-testid='LoginForm_Login_Button']").click()

print("zap")

time.sleep(10)

driver.close()