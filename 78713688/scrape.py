import requests
import json


def search_adviser_by_name(first, last):
    params = {
        "query": f"{first} {last}",
        "includePrevious": "true",
        "hl": "true",
        "nrows": "12",
        "start": "0",
        "r": "25",
        "sort": "score+desc",
        "wt": "json",
    }

    response = requests.get("https://api.adviserinfo.sec.gov/search/individual", params=params)

    records = response.json()["hits"]["hits"]

    return [record["_source"] for record in records]


info = search_adviser_by_name("Kelly", "Demers")

print(json.dumps(info, indent=2))
