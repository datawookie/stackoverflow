import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
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
    print(response.text)
