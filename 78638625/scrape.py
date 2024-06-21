import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
}

params = {
    "uiLang": "zh",
    "uiCity": "hongkong",
    "regionId": "0",
    "startAt": "0",
    "rows": "15",
    "pageToken": "CONST_DUMMY_TOKEN",
}

response = requests.get("https://www.openrice.com/api/v2/search", params=params, headers=headers)

data = response.json()

for result in data["paginationResult"]["results"]:
    print(result["name"])
    # print(result)
