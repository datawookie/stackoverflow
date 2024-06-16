import requests

# # Define the proxy
# proxy = {
#     'http': 'http://47.91.104.88:3128',
#     'https': 'http://47.91.104.88:3128',
# }

# # Send the request via the proxy
# r = requests.get("https://www.dubaipolice.gov.ae/", proxies=proxy, verify=False)

# # Print the response status code
# print(r.status_code)

# # Optionally, print more details about the response
# print(r.text)

r = requests.get("http://localhost:8000", verify=False)

print(r.status_code)
print(r.text)
