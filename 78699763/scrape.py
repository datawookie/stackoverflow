import requests
import pandas as pd
import re
from bs4 import BeautifulSoup

BASE_URL = "https://pubmed.ncbi.nlm.nih.gov"

QUERY = "Breast Cancer"
START_DATE = "2023/06/01"
END_DATE = "2023/12/31"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0",
}


def fetch_links(query, start_date, end_date):
    params = {
        "term": f'(({query})) AND (("{start_date}"[Date - Publication] : "{end_date}"[Date - Publication]))',
    }
    response = requests.get(BASE_URL, params=params, headers=HEADERS)
    soup = BeautifulSoup(response.text, "lxml")
    return [link["href"] for link in soup.select("a.docsum-title")]


def fetch_details(link):
    response = requests.get(link, headers=HEADERS)

    soup = BeautifulSoup(response.text, "lxml")
    title = soup.select_one("h1.heading-title").text.strip()
    authors = [author.text.strip() for author in soup.select("a.full-name")]
    pub_date = re.sub(";.*", "", soup.select_one("span.cit").text.strip())
    abstract = soup.select_one("div.abstract-content")
    if abstract:
        abstract = abstract.text.strip()

    return {"title": title, "authors": ", ".join(authors), "date": pub_date, "abstract": abstract}


if __name__ == "__main__":
    links = fetch_links(QUERY, START_DATE, END_DATE)
    data = []
    for link in links:
        # Make into absolute URL.
        link = BASE_URL + link
        print(link)
        try:
            details = fetch_details(link)
            data.append(details)
        except Exception as e:
            print(f"Error fetching details for {link}: {e}")
    data = pd.DataFrame(data)

    data.to_csv("pubmed_breast_cancer.csv", index=False)
