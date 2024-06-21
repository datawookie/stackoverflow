import requests

response = requests.get("https://charts-spotify-com-service.spotify.com/public/v0/charts")

data = response.json()

for entry in response.json()["chartEntryViewResponses"][0]["entries"]:
    meta = entry["trackMetadata"]
    entry = entry["chartEntryData"]

    track = meta["trackName"]
    artists = ", ".join([artist["name"] for artist in meta["artists"]])

    print(f"{entry['currentRank']:3} | {track:50} | {artists}")
