import requests

cookies = {
    "ssxmod_itna": "YqjxcCitDtqQu4BPGKiQ23BIS3vGaQeTrbKDlaOexWKGkD6DWP0Wr0eD0epm1mvgmhCt+QDrUWTImjR2PEC7DcGma=KxDTDbuPGSDG5DiDXGDGXKhhieDog4D1jD0KDWDYPGWeqDoDeoKD5xGCDeKD0xD8kx07DQ5DjYKDX=A7tUPD66cCPtBoXoyCK=2oqi4Hs=FOAE9tAWhqCmDTtAI3e2iKgiiKLahTZK4Krjw2DDpXMWhDD=",
    "webhash": "539806be-feeb-4e2c-b0e5-b13193df2783",
    "_gcl_au": "1.1.444485848.1718769072",
    "_ga_DS0L41EGL6": "GS1.1.1718793786.3.1.1718793821.0.0.0",
    "_ga": "GA1.2.975650866.1718769072",
    "tfstk": "foiKxugU4Z2C_MgoSvTiEAaE7GJDS0HEQXkfq7VhPfhthx53Pkql24H-9D0nFBl-25MnZWiux4C-Ofzotkal27Mqww2k8Y27N5GjKMVur3F-35uI8J9L7AZEj2jutBr-FjqviIxDmvkUzuODin2uzjZ7F3V5hkJjmurWiCxDmvkU4j2llTRKCde3E8Z7R8M_55yROJG7OP1_H-r7NbZWBlw4h9_7dua_f-J3kpFNdJI-yAF-mtR71gsSAyzLwvQlVgi_pyQEd5BhKceLJS4i7EFx2xHSxl3ANeMYbm4ofltdgJ3sHlN3cHs_xDkIlziXaaG-oXu4y0OdD5iEPDqsACsPzmmYEF10M8bpB0_PzywghdNb8Dd4Cn2TipaCzazuQRFDBBQPzyNUBSvQRa7z5ZC..",
    "ssxmod_itna2": "YqjxcCitDtqQu4BPGKiQ23BIS3vGaQeTrdD6OK87D0HxDQDL7peL9FeNQ=PMQ0bFPqRI04idam=BaXxOi4rHIzw+Kdw6PjRU89dqIDQ9dFDFqG7XeD==",
    "DefaultRegionIds": '{"hk":0,"mo":0}',
    "RegionId": "0",
    "isguest": "1",
    "autha": "gMDZN7w1h4fxpoesvPORmaeQhjDKR5AEMIrq6hBsjhrI_dSIho_bg6q9ZxBDx7acSVaz0lzgUzE4W7-chFZkf2crRdCZHuGfma8GcohWWpaHR0rGr81VLVxP7hF10Sdo4xO-kJnEw591mgpQVVxNHpTQdPOAAKdoaH1vzASd7A6OWdKV5WoJYyKw0bvSONLSsQd0JzQB9XZu5FIqmaChGBGtGbC2jr5LY6sfgAxQk17RlIx0hz7KsUQWLTEw1czNiv7JORgK3lEON_JgNpcwkUyYuB30UPkDViUxfxf8_SLXg_8GRewAV-cDUz_3jIxcGRzNdft-VN7li3uE8l8z-ke06xXadkUNf76VXohAugV0UTyFw8E2_0Sq4yGccQmURI2LSi7NbMlRLPp2UbTyFgJbNps",
    "authr": "aaOUmNzmzr707SVXmH7YG1rm7ptAUpljXyxHX9jyuJ50Lg30GxTSl7n4QSce2UF-W39o93jI0TMxMoUxjjIpvkekz6X1yruwSjaGs_1Gu_tw0yoBdARqrp1_M6JCGdxY1TmuPtbPyo6uTFZz7eW_-TCU796-zk5QNzm_DmURa2g3lDP-L1QUDf4z4cRx502ChQjB63WYs8AcffBDVIWk4n0k882OCEHxaeXKDMeUZc3GA2TZstiauAbTE1EN5mOQXoTXoz2oUbUti46STg9FdkEK49ZqtQbWmQJScZwq6F2eKaIGnNx4ONd6CN42930ociw4TdyWjllsR7tGFZcYN-K8i-4IUAvg4uF3WA1jDCgv7rcqchrxbnLCklheKYPV8Zi0Eb2wlJ4lf9culwtmGpnvzws",
    "authe": "gY2mWfWxv6Gj4fYeaikjGkfTDkSMa2EnhfzM1f0YVLZLOr7KE5sVLpPkLi71KJi2",
    "__utma": "183676536.975650866.1718769072.1718772436.1718793795.3",
    "__utmc": "183676536",
    "__utmz": "183676536.1718769079.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
    "_gid": "GA1.2.1307124666.1718769079",
    "_fbp": "fb.1.1718769082985.790676143172150851",
    "__eoi": "ID=f900759db74f69df:T=1718769083:RT=1718793795:S=AA-Afjb-Hssle0Qpz_YyVBA9nFpu",
    "__utmb": "183676536.2.10.1718793795",
    "__utmt_UA-652541-1": "1",
}

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    "Referer": "https://www.openrice.com/zh/hongkong/restaurants/district/%E5%B0%96%E6%B2%99%E5%92%80",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Connection": "keep-alive",
    # 'Cookie': 'ssxmod_itna=YqjxcCitDtqQu4BPGKiQ23BIS3vGaQeTrbKDlaOexWKGkD6DWP0Wr0eD0epm1mvgmhCt+QDrUWTImjR2PEC7DcGma=KxDTDbuPGSDG5DiDXGDGXKhhieDog4D1jD0KDWDYPGWeqDoDeoKD5xGCDeKD0xD8kx07DQ5DjYKDX=A7tUPD66cCPtBoXoyCK=2oqi4Hs=FOAE9tAWhqCmDTtAI3e2iKgiiKLahTZK4Krjw2DDpXMWhDD=; webhash=539806be-feeb-4e2c-b0e5-b13193df2783; _gcl_au=1.1.444485848.1718769072; _ga_DS0L41EGL6=GS1.1.1718793786.3.1.1718793821.0.0.0; _ga=GA1.2.975650866.1718769072; tfstk=foiKxugU4Z2C_MgoSvTiEAaE7GJDS0HEQXkfq7VhPfhthx53Pkql24H-9D0nFBl-25MnZWiux4C-Ofzotkal27Mqww2k8Y27N5GjKMVur3F-35uI8J9L7AZEj2jutBr-FjqviIxDmvkUzuODin2uzjZ7F3V5hkJjmurWiCxDmvkU4j2llTRKCde3E8Z7R8M_55yROJG7OP1_H-r7NbZWBlw4h9_7dua_f-J3kpFNdJI-yAF-mtR71gsSAyzLwvQlVgi_pyQEd5BhKceLJS4i7EFx2xHSxl3ANeMYbm4ofltdgJ3sHlN3cHs_xDkIlziXaaG-oXu4y0OdD5iEPDqsACsPzmmYEF10M8bpB0_PzywghdNb8Dd4Cn2TipaCzazuQRFDBBQPzyNUBSvQRa7z5ZC..; ssxmod_itna2=YqjxcCitDtqQu4BPGKiQ23BIS3vGaQeTrdD6OK87D0HxDQDL7peL9FeNQ=PMQ0bFPqRI04idam=BaXxOi4rHIzw+Kdw6PjRU89dqIDQ9dFDFqG7XeD==; DefaultRegionIds={"hk":0,"mo":0}; RegionId=0; isguest=1; autha=gMDZN7w1h4fxpoesvPORmaeQhjDKR5AEMIrq6hBsjhrI_dSIho_bg6q9ZxBDx7acSVaz0lzgUzE4W7-chFZkf2crRdCZHuGfma8GcohWWpaHR0rGr81VLVxP7hF10Sdo4xO-kJnEw591mgpQVVxNHpTQdPOAAKdoaH1vzASd7A6OWdKV5WoJYyKw0bvSONLSsQd0JzQB9XZu5FIqmaChGBGtGbC2jr5LY6sfgAxQk17RlIx0hz7KsUQWLTEw1czNiv7JORgK3lEON_JgNpcwkUyYuB30UPkDViUxfxf8_SLXg_8GRewAV-cDUz_3jIxcGRzNdft-VN7li3uE8l8z-ke06xXadkUNf76VXohAugV0UTyFw8E2_0Sq4yGccQmURI2LSi7NbMlRLPp2UbTyFgJbNps; authr=aaOUmNzmzr707SVXmH7YG1rm7ptAUpljXyxHX9jyuJ50Lg30GxTSl7n4QSce2UF-W39o93jI0TMxMoUxjjIpvkekz6X1yruwSjaGs_1Gu_tw0yoBdARqrp1_M6JCGdxY1TmuPtbPyo6uTFZz7eW_-TCU796-zk5QNzm_DmURa2g3lDP-L1QUDf4z4cRx502ChQjB63WYs8AcffBDVIWk4n0k882OCEHxaeXKDMeUZc3GA2TZstiauAbTE1EN5mOQXoTXoz2oUbUti46STg9FdkEK49ZqtQbWmQJScZwq6F2eKaIGnNx4ONd6CN42930ociw4TdyWjllsR7tGFZcYN-K8i-4IUAvg4uF3WA1jDCgv7rcqchrxbnLCklheKYPV8Zi0Eb2wlJ4lf9culwtmGpnvzws; authe=gY2mWfWxv6Gj4fYeaikjGkfTDkSMa2EnhfzM1f0YVLZLOr7KE5sVLpPkLi71KJi2; __utma=183676536.975650866.1718769072.1718772436.1718793795.3; __utmc=183676536; __utmz=183676536.1718769079.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _gid=GA1.2.1307124666.1718769079; _fbp=fb.1.1718769082985.790676143172150851; __eoi=ID=f900759db74f69df:T=1718769083:RT=1718793795:S=AA-Afjb-Hssle0Qpz_YyVBA9nFpu; __utmb=183676536.2.10.1718793795; __utmt_UA-652541-1=1',
}

params = {
    "uiLang": "zh",
    "uiCity": "hongkong",
}

response = requests.get(
    "https://www.openrice.com/api/v2/metadata/region/all", params=params, cookies=cookies, headers=headers
)

print(response.text)
