from requests_html import AsyncHTMLSession
from pprint import pprint
from typing import Any as any


async def get_url(url: str) -> any:
    print(url)
    return await session.get(url)


session = AsyncHTMLSession()

urls = ["https://python.org/", "https://reddit.com/", "https://google.com/"]
coroutines = [lambda url=url: get_url(url) for url in urls]

result = session.run(*coroutines)
pprint(result)
