import httpx
import pandas as pd

URL = "https://fantasyteamadvice.com/api/user/get-ownership"

json_data = {
    "sport": "mlb",
}

response = httpx.post(URL, json=json_data)

ownership = response.json()["ownership"]

ownership = pd.DataFrame(ownership)

ownership.to_csv("ownership.csv")
