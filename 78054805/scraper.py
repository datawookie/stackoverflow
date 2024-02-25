import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "From": "",
    "af-ac-enc-dat": "",
    "x-api-source": "pc",
}

params = {
    "filters": "9",
    "keyword": "funko",
    "locations": "Nacional",
    "noCorrection": "true",
    "page": "0",
    "sortBy": "relevancy",
}

with requests.Session() as session:
    response = session.get("https://shopee.com.br/search", params=params, headers=headers)
    print(response)
