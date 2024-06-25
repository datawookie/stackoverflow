import requests
from bs4 import BeautifulSoup
import pandas as pd

PAGES = 50
URL_BASE = "https://oig.hhs.gov"
URL_PATH = "/reports-and-publications/all-reports-and-publications/"
CSV_FILE = "OIG_Reports.csv"


def scrape_report_content(url):
    print(f"- {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    content = soup.find("div", class_="usa-prose pep-prose margin-top-6")
    if content:
        paragraphs = content.find_all("p")
        content = "\n".join([p.get_text(strip=True) for p in paragraphs]).strip()

    return content


data = []

for page in range(1, PAGES + 1):
    page_url = f"{URL_BASE}{URL_PATH}?page={page}"
    print(f"Scraping page {page}...")

    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, "html.parser")

    reports = soup.find_all("div", class_="usa-card__container")

    # Iterate over index pages, processing list of reports on each page.
    #
    for report in reports:
        link = report.find("a")
        audit, agency, date = [desc.get_text(strip=True) for desc in report.find_all("dd")]

        content = scrape_report_content(URL_BASE + link["href"])

        data.append(
            {
                "title": link.get_text(strip=True),
                "url": link,
                "report_number": audit,
                "agency": agency,
                "date": date,
                "content": content,
            }
        )

pd.DataFrame(data).to_csv(CSV_FILE, index=False)
