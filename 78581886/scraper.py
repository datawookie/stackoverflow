import re
import json
import time
import requests
from bs4 import BeautifulSoup

AUTHORISATION = "uYQSxBUgj-FzGSig35rhm8H-wyuit8P2qIRN9R9oFFU.eyJpbnN0YW5jZUlkIjoiMGQxYjlkZTItODJjZi00Mjg4LWIyNzMtMjcyN2YxZDQzNTZiIiwiYXBwRGVmSWQiOiIxNGRiZWYwNi1jYzQyLTU1ODMtMzJhNy0zYWJkNDRkYTQ5MDgiLCJtZXRhU2l0ZUlkIjoiNjk5NjMxMDgtNWI5MS00YWE2LWJjN2EtZjMwYWEyN2I5MDY3Iiwic2lnbkRhdGUiOiIyMDI0LTA2LTA3VDA0OjE0OjQzLjk1NloiLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6IjJkOWE4NmQ4LWQ1YTktNDk1Zi1iZmQ3LTljNzcwMTMyNWNhMCIsImJpVG9rZW4iOiI2NDhkYWNlYS1kOTVlLTA4MmUtMGUwOS1kNDJkNTNhZmE1MGMiLCJzaXRlT3duZXJJZCI6IjIxNDJkOGM4LTUzZWItNDUwZS05NGVmLTY2NDk1NTljOTE5MSJ9"

params = {
    "lang": "en",
    "dateNumberFormat": "en-us",
    "isPrimaryLanguage": "true",
    "pageId": "awj6y",
    "compId": "TPASection_l94pvaso",
    "viewerCompId": "TPASection_l94pvaso",
    "siteRevision": "6251",
    "viewMode": "site",
    "deviceType": "desktop",
    "locale": "en",
    "tz": "America/Los_Angeles",
    "regionalLanguage": "en",
    "width": "1395",
    "height": "8656",
    "instance": "lzISSV24nhE8UVR4a7tpdOKz3A-vBS56PrcDZjqiqH4.eyJpbnN0YW5jZUlkIjoiOTczYzhjNmEtMzA4OC00ZDU1LTg0YTctY2YzMGE5NmNiNjM5IiwiYXBwRGVmSWQiOiIxNGRiZWZkMi0wMWI0LWZiNjEtMzJhNy0zYWJkNDRkYTQ5MDgiLCJtZXRhU2l0ZUlkIjoiNjk5NjMxMDgtNWI5MS00YWE2LWJjN2EtZjMwYWEyN2I5MDY3Iiwic2lnbkRhdGUiOiIyMDI0LTA2LTA3VDAzOjUzOjUwLjI0M1oiLCJkZW1vTW9kZSI6ZmFsc2UsImFpZCI6IjJkOWE4NmQ4LWQ1YTktNDk1Zi1iZmQ3LTljNzcwMTMyNWNhMCIsImJpVG9rZW4iOiJmZWFhYmQ2Mi02YjE5LTA3ZjMtMzhkZC0zYzNhMGIxNzI2NWUiLCJzaXRlT3duZXJJZCI6IjIxNDJkOGM4LTUzZWItNDUwZS05NGVmLTY2NDk1NTljOTE5MSJ9",
    "currency": "USD",
    "currentCurrency": "USD",
    "commonConfig": '{"brand":"wix","host":"VIEWER","bsi":"056bd407-5120-46de-88c2-65e051ee317a|1","BSI":"056bd407-5120-46de-88c2-65e051ee317a|1"}',
    "currentRoute": "./members",
    "target": "_top",
    "section-url": "https://www.iahsp.com/members/",
    "vsi": "1c2dc3c9-baf6-48d0-9844-89cc85557e75",
}

response = requests.get(
    "https://members.wixapps.net/_api/members-area/app/members",
    params=params,
)

soup = BeautifulSoup(response.text, "lxml")

# The data is in a <script> body.
script = soup.select_one("body script")
# Extract relevant part of <script> content.
match = re.search(r"window\.__INITIAL_STATE__ = (\{.*?\});", script.get_text(), re.S)

data = json.loads(match.group(1))

# Get UIDs for members.
#
UID = [member["uid"] for member in data["members"]["map"].values()]


def get_member(uid):
    headers = {
        "authorization": AUTHORISATION,
    }

    json_data = {
        "fileName": "server/profile.api",
        "functionName": "getInitialData",
        "args": [
            {
                "showAboutSection": True,
                "showJoinDate": True,
                "showBadgesSection": True,
                "showOverviewSection": True,
                "showBlogPostsSection": True,
                "showCommentsStats": True,
                "showLikesReceivedStats": True,
                "showTopCommentsStats": True,
                "currentMemberId": None,
                "viewedMemberId": uid,
                "postsPerPage": 3,
                "language": "en",
                "isRTL": False,
                "isMultilingualEnabled": True,
                "isMembersAboutV2Enabled": False,
                "shouldAddPostListToSeoData": False,
                "shouldAddRicosContentToSeoData": False,
                "fetchMemberFieldSet": "FULL",
            },
        ],
    }

    response = requests.post(
        "https://www.iahsp.com/serverless-yoshi-members-about-ooi/members-about-ooi-93fbd3a84c07138e5078ad7439ce5067/_api_/server/profile.api",
        headers=headers,
        json=json_data,
    )

    member = response.json()["payload"]

    def get_field(field):
        key = "customfields.system." + field

        for field in member["member"]["customProfile"]["fields"]:
            if field["key"] == key:
                return field["value"]
        else:
            raise RuntimeError(f"Unable to find {field}.")

    print({"first": get_field("firstname"), "last": get_field("lastname"), "email": get_field("email")})


for uid in UID:
    # Be gentle.
    time.sleep(5)

    get_member(uid)
