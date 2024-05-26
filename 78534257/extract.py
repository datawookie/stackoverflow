import json
import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/125.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Referer": "https://silkroadmed.com/",
    "Sec-Fetch-Dest": "script",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "cross-site",
}

params = {
    "callback": "slw",
    "_": "1716699895443",
}

response = requests.get(
    "https://cdn.storelocatorwidgets.com/json/AJ587baQBwcvO8ZBAoQKFx0r5DhPhcub",
    params=params,
    headers=headers,
)

data = response.text

# The JSON is wrapped in "slw(...)".
#
data = re.sub("^slw\(|\)$", "", data)

data = json.loads(data)

with open("hospital-locations.json", "wt") as file:
    json.dump(data, file, indent=2)

with open("hospital-locations.csv", "wt") as file:
    file.write("name,lat,lon\n")
    for location in data["stores"]:
        file.write('"%s", %f, %f\n' % (location["name"], location["data"]["map_lat"], location["data"]["map_lng"]))
