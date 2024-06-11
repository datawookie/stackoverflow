import requests

cookies = {
    'A1': 'd=AQABBAviZmYCEM1Y9pBy3PswxEwfNv42rMsFEgABCAExaGaZZvbPb2UB9qMAAAcICOJmZjSu1io&S=AQAAAlTFeeTgnvCD4S1zkgBE3CY',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5'
}

params = {
    'crumb': 'uRdMhpzZPfD',
    'lang': 'en-US',
    'region': 'US',
    'corsDomain': 'finance.yahoo.com',
}

json_data = {
    'sortType': 'ASC',
    'entityIdType': 'earnings',
    'sortField': 'companyshortname',
    'includeFields': [
        'ticker',
        'companyshortname',
        'eventname',
        'startdatetime',
        'startdatetimetype',
        'epsestimate',
        'epsactual',
        'epssurprisepct',
        'timeZoneShortName',
        'gmtOffsetMilliSeconds',
    ],
    'query': {
        'operator': 'and',
        'operands': [
            {
                'operator': 'gte',
                'operands': [
                    'startdatetime',
                    '2024-06-10',
                ],
            },
            {
                'operator': 'lt',
                'operands': [
                    'startdatetime',
                    '2024-06-11',
                ],
            },
            {
                'operator': 'eq',
                'operands': [
                    'region',
                    'us',
                ],
            },
        ],
    },
    'offset': '0',
    'size': 100,
}

response = requests.post(
    'https://query1.finance.yahoo.com/v1/finance/visualization',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)

print(response.text)

import json

with open("goo.json", "wt") as file:
    file.write(json.dumps(response.json(), indent=2))

for entry in response.json()["finance"]["result"][0]["documents"]