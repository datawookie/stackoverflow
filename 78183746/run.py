from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")

print("Launch Chrome.")
driver = webdriver.Chrome(options=options)

print("Get www.example.com.")
driver.get("http://www.example.com")

print("Close Chrome.")
driver.quit()
