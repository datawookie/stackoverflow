import time
import undetected_chromedriver as uc
import pandas as pd
from bs4 import BeautifulSoup


URL = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/"

driver = uc.Chrome(headless=False, use_subprocess=True)

driver.get(URL)

# Wait for page to fully load. Could actually wait for a specific element.
time.sleep(5)

soup = BeautifulSoup(driver.page_source, "lxml")

data = []

for row in soup.select_one("table.data-table > tbody").select("tr"):
    data.append(
        {
            "rank": row.select_one("td.csr-col--rank .data-table__value").text,
            "school": row.select_one("td.csr-col--school-name .data-table__value").text,
            "degree": row.select_one("td.csr-col--school-type .data-table__value").text,
            "early": row.select_one("td:nth-of-type(4) .data-table__value").text,
            "mid": row.select_one("td:nth-of-type(5) .data-table__value").text,
        }
    )

driver.quit()

data = pd.DataFrame(data)
print(data)
