import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    "Content-Type": "application/json; charset=utf-8",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Referer": "https://www.macmap.org/en//query/results?reporter=826&partner=710&product=010229&level=6",
    # 'Cookie': 'persistence=80564234.47873.0000; TS01b84bf4=01aafb0fddf8579272f869abf2f25464fc1c21a30998ae6b4d41008a6a3e5f1ad6c62803504961570485ebb09b055bd182622070f529d495e33a7e628717001df7a6c9f8b219b16922576ac0081ba7d7e3842c94144fcf05af9a8345163f89c6080c2e924d; ASP.NET_SessionId=gqxtfc3ninuqbwaw3pltmpwv; Culture=en; _ga_4PB9L9S57N=GS1.1.1721276851.1.1.1721276919.0.0.0; _ga=GA1.1.1456660232.1721276851',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
}

params = {
    "countryCode": "826",
    "level": "8",
    "code": "010229",
}

response = requests.get("https://www.macmap.org/api/v2/ntlc-products", params=params, headers=headers)

print(response.text)
