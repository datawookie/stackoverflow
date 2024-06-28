import requests

headers = {
    "Content-Type": "application/json; charset=utf-8",
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
