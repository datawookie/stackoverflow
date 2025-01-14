from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

URL = "https://www.sec.gov/Archives/edgar/data/1346824/000110465924035606/0001104659-24-035606-index.html"

DRIVER_PATH = "/usr/bin/chromedriver"

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

service = Service(executable_path=DRIVER_PATH)

driver = webdriver.Chrome(service=service, options=options)

driver.get(URL)

link = driver.find_element(By.XPATH, '//*[@id="formDiv"]/div/table/tbody/tr[2]/td[3]')

print(link)
print(link.text)


driver.close()
