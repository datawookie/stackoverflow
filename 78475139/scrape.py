import requests
from bs4 import BeautifulSoup, Comment
import pandas as pd
from io import StringIO

url = "https://fbref.com/en/comps/22/gca/Major-League-Soccer-Stats"

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

comments = soup.find_all(string=lambda text: isinstance(text, Comment))

for comment in comments:
    # Check if the comment contains the target <div>.
    if "div_stats_gca" in comment:
        # Parse the comment as HTML and extract target <div>.
        div = BeautifulSoup(comment, "html.parser").find(id="div_stats_gca")

        df = pd.read_html(StringIO(str(div)))[0]
        print(df.iloc[:, :6])
else:
    print("Unable to find table.")
