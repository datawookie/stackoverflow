from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Remote(
  "http://127.0.0.1:4444/wd/hub",
  options=options
)

driver.get('https://www.forexfactory.com/calendar?week=this')

import time
time.sleep(10)

try:
    high_impact_news = high_impact_rows = driver.find_elements(By.XPATH, "//tr[.//span[contains(@class, 'icon--ff-impact-red')]]")

    for row in high_impact_news:
        print("==================================================")
        date = row.find_element(By.XPATH, "preceding-sibling::tr[.//td[@rowspan]][1]//span[@class='date']").text
        title = row.find_element(By.XPATH, ".//span[@class='calendar__event-title']").text

        try:
            # Time in same row.
            time = row.find_element(By.XPATH, ".//td[@class='calendar__cell calendar__time']//span")
        except:
            # Time in spanning row.
            time = row.find_element(By.XPATH, "preceding-sibling::tr[.//td[@class='calendar__cell calendar__time']][1]//span[not(contains(@class, 'icon'))]")

        # Remove line break from date.
        date = date.replace("\n", " ")

        print(title)
        print(date)
        print(time.text)

    print(f"Found {len(high_impact_news)} high impact news events")

    if high_impact_news:
        print("High impact news found")
    else:
        print("No high impact news found")
finally:
    driver.quit()
