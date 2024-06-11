import requests
import time
from bs4 import BeautifulSoup

DATE = "2024-06-07"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0",
    "Accept": "*/*",
    "authorization": "Bearer none",
}

params = {
    "operationName": "meetingsIndexByStartEndDate",
    "variables": '{"startDate": "' + DATE + '", "endDate": "' + DATE + '", "limit": 100}',
    "extensions": '{"persistedQuery": {"version": 1, "sha256Hash": "998212fede87c9261e0f18e9d8ced2ed04a915453dcd64ae1b5cf5a72cf25950"}}',
}

response = requests.get("https://puntapi.com/graphql-horse-racing", params=params, headers=headers)

races = response.json()

for group in races["data"]["meetingsGrouped"]:
    for meeting in group["meetings"]:
        for event in meeting["events"]:
            time.sleep(5)
            print("🟦 "+meeting["name"]+" — "+event["name"]+"\n")

            URL = "https://www.racenet.com.au/results/horse-racing/"+meeting["slug"]+"/"+event["slug"]

            print("URL: "+URL+"\n")

            response = requests.get(URL, headers=headers)

            soup = BeautifulSoup(response.text, "html.parser")

            names = soup.select("h4.selection-result__info-competitor-name")

            for name in names:
                print(name.get_text().strip())

            print()