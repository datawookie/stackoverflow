import requests
from datetime import datetime
import json

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
}

response = requests.get(
    "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson",
    headers=headers,
)

quakes = []
#
for quake in response.json()["features"]:
    # There a LOT of information in quake, but just extract a few elements for illustration.
    quakes.append(
        {
            "magnitude": quake["properties"]["mag"],
            "location": quake["geometry"]["coordinates"],
            "time": datetime.fromtimestamp(quake["properties"]["time"] / 1000).strftime("%Y-%m-%d %H:%M:%S"),
        }
    )

print(json.dumps(quakes, indent=2))
