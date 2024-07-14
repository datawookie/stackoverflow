import re
import requests
from pandas import DataFrame

URL = "https://www.milwaukeetool.com/products/power-tools/drilling/drill-drivers"

# GET CATEGORY ID -------------------------------------------------------------

response = requests.get(URL)

pattern = r"\\\"page_id\\\":\\\"{(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})}\\\""

category_id = re.search(pattern, response.text).groups()[0]

# PULL CATEGORY FROM API ------------------------------------------------------

data = {
    "language": "en",
    "returnAll": True,
    "categories": category_id,
}

response = requests.post("https://www.milwaukeetool.com/api/v1/products/listing", json=data)


results = response.json()["data"]["results"]

products = []

for result in results:
    products.append(
        {
            "sku": result["sku"],
            "description": result["title"],
        }
    )

products = DataFrame(products)
print(products)
