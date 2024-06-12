from bs4 import BeautifulSoup
import requests
import re
import time

url = 'https://minecraft.wiki/w/Block'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

blocks = []
for li in soup.find_all('li'):
    name_element = li.find('a', class_='mw-redirect')
    
    if name_element:
        name = name_element.text.strip()
        url = 'https://minecraft.wiki/w/' + re.sub(r'\s+', '_', name)
    
        blocks.append({'name': name, 'url': url})

images = []

for block in blocks:
    response = requests.get(block['url'])
    soup = BeautifulSoup(response.text, 'html.parser')

    for img in soup.select("img.mw-file-element"):
        # Get src attribute from <img> tag.
        src = img.get("src")
        # Strip off any parameters.
        src = re.sub("\?.*$", "", src)
        url = "https://minecraft.wiki"+src
        print(url)
        images.append({'image:' : url})

    # Pause.
    time.sleep(10)


