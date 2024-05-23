import requests

cookies = {
    "set_num_visits_per_set": "1",
    "qi5": "7tj44f4o7tne%3AuitkbAucX19E3jC2.HbW",
    "qtkn": "GfE6wDxQTvXAyC3jzuusbK",
    "fs": "sdvowz",
    "_pxhd": "dd282a77a68d44b16d44a72dae5cb65e0f34232721c9ddab19cc71c18235b664:648af3fd-1815-11ef-89a7-291b876c10b1",
    "__cfruid": "9e85c4aad66d3723447144c735661a2776312bd6-1716366563",
    "_cfuvid": "L7_ezVXJw72ZwnE3l4.nfChV7vPW9j_lmqvy3aKnr48-1716366563728-0.0.1.1-604800000",
    "_sp_id.424b": "13da0bd3-3d11-4457-bc9f-eb489f9a4da4.1716366563.2.1716388962.1716366575.7d5407e3-9e14-4217-b128-2284e4984904.641704a1-fc2e-4340-becb-43fdf0d4117a.95f5e9da-28a7-41e5-afe0-ddeb774968e7.1716388940587.4",
    "session_landing_page": "Homepage%2Findex",
    "sp": "f5a66a10-8431-4de4-a8ea-a869657f315b",
    "cf_clearance": "XDaWEsWQsWl8tntYlDMNg623a45KbWENYdkX1ly96ww-1716366564-1.0.1.1-ihj6H.MUPE3AnDUcelMAGkGqL26DhpthWdm4vTvKlBYDJhRqLO9Oe9xUx27XJ8Qk_RTU4M.F5r4znbQmlmA1mw",
    "_ga_VG8TWT63ZN": "GS1.1.1716388941.2.0.1716388941.0.0.0",
    "_ga": "GA1.2.259148257.1716366564",
    "_ga_BGGDEZ0S21": "GS1.1.1716388941.2.0.1716388941.0.0.0",
    "pxcts": "657e990c-1815-11ef-aff4-6a230558b30d",
    "_pxvid": "648af3fd-1815-11ef-89a7-291b876c10b1",
    "_gid": "GA1.2.754743159.1716366564",
    "_tt_enable_cookie": "1",
    "_ttp": "qhsndFayUTn5dZVKCI4nCU97zPO",
    "_gcl_au": "1.1.1625638828.1716366564",
    "afUserId": "b483430c-bbdb-43fd-9e93-e184b3a7e81e-p",
    "AF_SYNC": "1716366564696",
    "OptanonConsent": "isGpcEnabled=0&datestamp=Wed+May+22+2024+15%3A42%3A22+GMT%2B0100+(British+Summer+Time)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0004%3A1%2CC0002%3A1%2CN01%3A1%2CV2STACK42%3A0&AwaitingReconsent=false",
    "g_state": '{"i_p":1716373766900,"i_l":1}',
    "app_session_id": "a48293bf-77fb-4697-8ef0-8261d50a4a8a",
    "__cf_bm": "iLSv.OwP32dPC6klVXrBG2krYTxP0m9qGw4jV9jcUwE-1716388940-1.0.1.1-_X_7qO64Dzoa8Gak45zL.oM0heokdH8N3HhoaGP7wc1_51lGpm_x3.u6Nqc0EpqkYMGmcS61y_8jSp9ouaBm6Q",
    "_sp_ses.424b": "*",
    "chr_3p_state_logged": "true",
    "qmeasure__persistence": "%7B%2292%22%3A%2200000100%22%7D",
    "_gat_UA-1203987-1": "1",
    "_px3": "dd57ae3d5b73e8db6ad2bfd92038a22b122b2784456f6440ccb8aa4b973205d6:FEofBvi77OuESXL8oGuimBRRZBW9MtGF367bpR9VQNo7kaBVTdBPpn8lKLImtbaUfJ/AUoRBpE76FcSsRSnTqQ==:1000:nwT06tpECS0XC2N9/YvUMW/UgclSr2Q0SjWM+Ko6E5y4ljxoYwDOb1PyooLKZVMEPuxZr+4GnmAVmNUBsEjpKFohCAi/4w/9iazsN5gK0SlK7YHGdnGAtv7g2MYqvqV+konFBR3FZeL1Rb09PUoPrAkxuKGEheRKis1ALcfwR5OXzACrRuo0AZnvWVF7zvlKVuXTDATc3T6LpyCpSuUIIsIpzoWH7R2/bl+Rn5q6z1Y=",
    "_lr_geo_location": "GB",
    "_sharedID": "c05f38a1-8295-447a-a7a9-2780f71d9192",
    "_sharedID_cst": "RCzLLJoslg%3D%3D",
}

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    # 'Accept-Encoding': 'gzip, deflate, br',
    "Connection": "keep-alive",
    # 'Cookie': 'set_num_visits_per_set=1; qi5=7tj44f4o7tne%3AuitkbAucX19E3jC2.HbW; qtkn=GfE6wDxQTvXAyC3jzuusbK; fs=sdvowz; _pxhd=dd282a77a68d44b16d44a72dae5cb65e0f34232721c9ddab19cc71c18235b664:648af3fd-1815-11ef-89a7-291b876c10b1; __cfruid=9e85c4aad66d3723447144c735661a2776312bd6-1716366563; _cfuvid=L7_ezVXJw72ZwnE3l4.nfChV7vPW9j_lmqvy3aKnr48-1716366563728-0.0.1.1-604800000; _sp_id.424b=13da0bd3-3d11-4457-bc9f-eb489f9a4da4.1716366563.2.1716388962.1716366575.7d5407e3-9e14-4217-b128-2284e4984904.641704a1-fc2e-4340-becb-43fdf0d4117a.95f5e9da-28a7-41e5-afe0-ddeb774968e7.1716388940587.4; session_landing_page=Homepage%2Findex; sp=f5a66a10-8431-4de4-a8ea-a869657f315b; cf_clearance=XDaWEsWQsWl8tntYlDMNg623a45KbWENYdkX1ly96ww-1716366564-1.0.1.1-ihj6H.MUPE3AnDUcelMAGkGqL26DhpthWdm4vTvKlBYDJhRqLO9Oe9xUx27XJ8Qk_RTU4M.F5r4znbQmlmA1mw; _ga_VG8TWT63ZN=GS1.1.1716388941.2.0.1716388941.0.0.0; _ga=GA1.2.259148257.1716366564; _ga_BGGDEZ0S21=GS1.1.1716388941.2.0.1716388941.0.0.0; pxcts=657e990c-1815-11ef-aff4-6a230558b30d; _pxvid=648af3fd-1815-11ef-89a7-291b876c10b1; _gid=GA1.2.754743159.1716366564; _tt_enable_cookie=1; _ttp=qhsndFayUTn5dZVKCI4nCU97zPO; _gcl_au=1.1.1625638828.1716366564; afUserId=b483430c-bbdb-43fd-9e93-e184b3a7e81e-p; AF_SYNC=1716366564696; OptanonConsent=isGpcEnabled=0&datestamp=Wed+May+22+2024+15%3A42%3A22+GMT%2B0100+(British+Summer+Time)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0004%3A1%2CC0002%3A1%2CN01%3A1%2CV2STACK42%3A0&AwaitingReconsent=false; g_state={"i_p":1716373766900,"i_l":1}; app_session_id=a48293bf-77fb-4697-8ef0-8261d50a4a8a; __cf_bm=iLSv.OwP32dPC6klVXrBG2krYTxP0m9qGw4jV9jcUwE-1716388940-1.0.1.1-_X_7qO64Dzoa8Gak45zL.oM0heokdH8N3HhoaGP7wc1_51lGpm_x3.u6Nqc0EpqkYMGmcS61y_8jSp9ouaBm6Q; _sp_ses.424b=*; chr_3p_state_logged=true; qmeasure__persistence=%7B%2292%22%3A%2200000100%22%7D; _gat_UA-1203987-1=1; _px3=dd57ae3d5b73e8db6ad2bfd92038a22b122b2784456f6440ccb8aa4b973205d6:FEofBvi77OuESXL8oGuimBRRZBW9MtGF367bpR9VQNo7kaBVTdBPpn8lKLImtbaUfJ/AUoRBpE76FcSsRSnTqQ==:1000:nwT06tpECS0XC2N9/YvUMW/UgclSr2Q0SjWM+Ko6E5y4ljxoYwDOb1PyooLKZVMEPuxZr+4GnmAVmNUBsEjpKFohCAi/4w/9iazsN5gK0SlK7YHGdnGAtv7g2MYqvqV+konFBR3FZeL1Rb09PUoPrAkxuKGEheRKis1ALcfwR5OXzACrRuo0AZnvWVF7zvlKVuXTDATc3T6LpyCpSuUIIsIpzoWH7R2/bl+Rn5q6z1Y=; _lr_geo_location=GB; _sharedID=c05f38a1-8295-447a-a7a9-2780f71d9192; _sharedID_cst=RCzLLJoslg%3D%3D',
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

response = requests.get("https://quizlet.com/173246204/mgmt-final-exam-flash-cards/", cookies=cookies, headers=headers)

print(response.text)
