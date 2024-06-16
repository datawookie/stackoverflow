import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
}

params = {
    # Grant County, New Mexico
    "g": "050XX00US35017",
    # Los Angeles County, California
    # 'g': '050XX00US06037',
}

response = requests.get("https://data.census.gov/api/profile/content/highlights", params=params, headers=headers)

print(json.dumps(response.json(), indent=2))

params = {
    "g": "050XX00US35017",
    "includeHighlights": "false",
}

response = requests.get("https://data.census.gov/api/profile/metadata", params=params, headers=headers)

print(response.json()["header"]["description"])
