import requests
import json

DATE = "2024-06-07"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0",
    "Accept": "*/*",
    "authorization": "Bearer none",
}

params = {
    "operationName": "meetingsIndexByStartEndDate",
    "variables": '{"startDate": "' + DATE + '", "endDate": "' + DATE + '", "limit": 100}',
    "extensions": '{"persistedQuery": {"version": 1, "sha256Hash": "998212fede87c9261e0f18e9d8ced2ed04a915453dcd64ae1b5cf5a72cf25950"}}',
}

response = requests.get("https://puntapi.com/graphql-horse-racing", params=params, headers=headers)

with open(f"race-data-{DATE}.json", "wt") as file:
    file.write(json.dumps(response.json(), indent=2))
