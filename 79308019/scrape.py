import time
from selenium import webdriver
from bs4 import BeautifulSoup

URL = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/"

driver = webdriver.Chrome()

driver.get(URL)
driver.implicitly_wait(10)

time.sleep(10)

soup = BeautifulSoup(driver.page_source, "lxml")
print(soup)

driver.quit()
