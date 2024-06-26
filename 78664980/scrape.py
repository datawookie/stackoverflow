import requests
import lxml.html
import sys

response = requests.get("https://jeffersonmo-assessor.devnetwedge.com/parcel/view/01401903003039/2023")

with open("page.html", "wt") as file:
    file.write(response.text)

tree = lxml.html.fromstring(response.text)

try:
    overview = tree.xpath('//div[@id="overview-body"]')[0]
except IndexError:
    print("Unable to locate overview.")
    sys.exit(1)

try:
    number = overview.xpath('.//td[@class="col-xs-6"]/div[@class="inner-value"]')[0].text_content()
except IndexError:
    print("Unable to locate parcel number.")
    sys.exit(1)

print(number)
