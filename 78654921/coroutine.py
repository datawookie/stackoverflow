from requests_html import AsyncHTMLSession
from pprint import pprint
from typing import Any as any

# async def async_get_url(session: AsyncHTMLSession, url: str) -> any:
#     print(f"Fetching: {url}")
#     #   s = a_hs()
#     #   r = await s.get(url)

#     #   return r
#     return await session.get(url)

# # async def main():
# #   urls = ('https://python.org/', 'https://reddit.com/', 'https://google.com/')
# #   for url in urls:
# #      print(url)
# #      await async_get_url(url)
# #   print("MAIN")

# # if __name__ == "__main__":
# # #   result = a_hs.run(*[async_get_url(url) for url in urls])

# # #   pprint(result)
# #     session = AsyncHTMLSession()
# #     session.run(main)
# #     # a_hs.run(main)

# async def main():
#     session = AsyncHTMLSession()
#     urls = ('https://python.org/', 'https://reddit.com/', 'https://google.com/')
#     tasks = [async_get_url(session, url) for url in urls]
#     responses = await asyncio.gather(*tasks)
    
#     for response in responses:
#         print(f"URL: {response.url}, Status Code: {response.status_code}")

# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(main())

session = AsyncHTMLSession()

# async def get_pythonorg():
#     print("A")
#     r = await session.get('https://python.org/')

# async def get_reddit():
#     print("B")
#     r = await session.get('https://reddit.com/')

# async def get_google():
#     print("C")
#     r = await session.get('https://google.com/')

# result = session.run(get_pythonorg, get_reddit, get_google)
# session.run(*[lambda: x for x in [get_pythonorg, get_reddit, get_google]])

# # List of coroutine functions
# coroutines = [get_pythonorg, get_reddit, get_google]

# coroutines = [get_url(url) for url in ('https://python.org/', 'https://reddit.com/', 'https://google.com/')]

# # # Run the coroutines
# result = session.run(*coroutines)

async def get_url(url: str) -> any:
    print(url)
    r = await session.get(url)

def get_url_coro(url: str):
    async def coro():
        await get_url(url)
    return coro

# List of coroutine functions
urls = ['https://python.org/', 'https://reddit.com/', 'https://google.com/']
coroutines = [get_url_coro(url) for url in urls]

# Run the coroutines
result = session.run(*coroutines)