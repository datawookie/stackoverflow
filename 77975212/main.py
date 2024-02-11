import os
import base64
import requests
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from dotenv import load_dotenv

load_dotenv()
#
# The .env file contains definitions for the following environment variables:
#
PROXY_USER = os.environ["PROXY_USER"]
PROXY_PWRD = os.environ["PROXY_PWRD"]
PROXY_HOST = os.environ["PROXY_HOST"]
PROXY_PORT = os.environ["PROXY_PORT"]
#
# The host and port are from the proxy list on webshare.io.

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]

user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

ATTEMPTS = 3
TIMEOUT = 30

def request_with_proxy(url, headers={}):
    headers["User-Agent"] = user_agent_rotator.get_random_user_agent()
    try:
        proxy_url = f'http://{PROXY_USER}:{PROXY_PWRD}@{PROXY_HOST}:{PROXY_PORT}'
        proxies = {
            'http': proxy_url,
            'https': proxy_url
        }
    except:
        raise TypeError("Missing environment variables!")

    print(url)
    print(headers)

    for _ in range(ATTEMPTS):
        try:
            response = requests.get(url, headers=headers, proxies=proxies, timeout=TIMEOUT)
            print(response.status_code)
            return response
        except Exception as E: print(E)

if __name__ == "__main__":
    request_with_proxy("https://github.com/davidteather/everything-web-scraping/stargazers")
    request_with_proxy("https://kleinanzeigen.de/")
