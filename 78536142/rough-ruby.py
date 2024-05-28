import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Origin": "https://bazaartracker.com",
}


def get_prices(item):
    params = {
        "query": item,
    }

    response = requests.get("https://api.bazaartracker.com/search", params=params, headers=headers)

    item = response.json()[0]

    return {
        "name": item["item"]["name"],
        "buy": item["product"]["buyprice"],
        "sell": item["product"]["sellprice"],
    }


print(get_prices("rough ruby"))
print(get_prices("enchanted carrot on a stick"))
print(get_prices("super compactor 3000"))
