import requests

url = "https://www.anbima.com.br/informacoes/est-termo/CZ-down.asp"

form_data = {"escolha": "2", "Idioma": "PT", "saida": "xls", "Dt_Ref_Ver": "20240607", "Dt_Ref": "14/06/2024"}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

response = requests.post(url, data=form_data, headers=headers)

if response.status_code == 200:
    print("Form submitted successfully.")
    with open("downloaded_file.xls", "wb") as f:
        f.write(response.content)
else:
    print(f"Failed to submit form. Status code: {response.status_code}")
    print(response.text)
