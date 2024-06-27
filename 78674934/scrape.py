import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0",
    "Accept": "text/plain, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    "Content-Type": "application/json; charset=utf-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://pjenlinea3.poder-judicial.go.cr",
    "Connection": "keep-alive",
    "Referer": "https://pjenlinea3.poder-judicial.go.cr/estadisticasoij/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Priority": "u=1",
}

data = {
    "pJson": {
        "TN_FechaInicio": 20240101,
        "TN_FechaFinal": 20240625,
        "TC_Provincias": "2",
        "TC_Cantones": "0",
        "TC_Distritos": "0",
        "TC_Delito": "2",
        "TC_Victima": "1,2,3,4,5",
        "TC_Modalidades": "0",
    },
    "pExtension": "csv",
}
# Data needs to be a string.
data["pJson"] = str(data["pJson"])
data = str(data)

response = requests.post(
    "https://pjenlinea3.poder-judicial.go.cr/estadisticasoij/Home/obtenerDatosDescargas",
    headers=headers,
    data=data,
)

with open("pjenlinea3.csv", "wt") as file:
    file.write(response.text)
