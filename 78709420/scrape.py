import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://jito.org"

i = 0

profiles = []

# while True:
while i < 60:
    url = BASE_URL + f"/members?start={i}"
    print(url)
    response = requests.get(url)
    print(f"- Status: {response.status_code}.")

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.select("h3.name > a")
    print(f"- Got {len(links)} links.")

    # Stop when there are no more profiles.
    if len(links) == 0:
        break

    for link in links:
        profiles.append({"name": link.text, "url": BASE_URL + link["href"]})

    # Go easy on the site.
    time.sleep(3)

    i += 20

df = pd.DataFrame(profiles)
print(df)
df.to_csv("jito-directory.csv", index=False)
