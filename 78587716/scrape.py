import os
import json

import serpapi
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("SERPAPI_KEY")
client = serpapi.Client(api_key=api_key)

results = client.search({"engine": "google_maps_reviews", "type": "search", "place_id": "ChIJidRKt32YVogRN6fEPG9Kuho"})

# Convert results to string before parsing JSON.
#
data = json.loads(str(results))

with open("results.json", "wt") as file:
    file.write(json.dumps(data, indent=2))
