from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

driveroptions = webdriver.ChromeOptions()
driveroptions.add_argument("--headless")
driver = webdriver.Remote(command_executor="http://127.0.0.1:4444", options=driveroptions, keep_alive=False)
driver.get("https://www.example.com")

print(driver.find_element(By.TAG_NAME, "h1").text)

driver.quit()
