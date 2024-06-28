import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", options=options)

driver.get(
    "https://workforcenow.adp.com/mascsr/default/mdf/recruitment/recruitment.html?cid=39bc5efc-a576-4a4d-83eb-32e95d4e96c8&ccId=19000101_000001&lang=en_US&selectedMenuKey=CurrentOpenings"
)

jobs_list = []

# Wait for job listings to show.
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".current-openings-item")))
# Get all job listings.
job_listings = driver.find_elements(By.CSS_SELECTOR, ".current-openings-item")

with open("page.html", "wt") as file:
    file.write(driver.page_source)

for job in job_listings:
    title = job.find_element(By.CSS_SELECTOR, "span.current-opening-title").text
    location = job.find_element(By.CSS_SELECTOR, "label.current-opening-location-item").text
    date = job.find_element(By.CSS_SELECTOR, "span.current-opening-post-date").text

    jobs_list.append(
        {
            "Company": "Metrea",
            "Job Title": title,
            "Job Link": None,
            "Location": location,
            "Date Posted": date,
            "ID": None,
            "Category": None,
            "Job Type": None,
        }
    )

driver.quit()

print(json.dumps(jobs_list, indent=2))
