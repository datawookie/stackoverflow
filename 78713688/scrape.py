import requests
from bs4 import BeautifulSoup


def search_adviser_by_name(first_name, last_name):
    search_url = "https://adviserinfo.sec.gov/IAPD/Individual/Search/Search"
    search_params = {
        'ADVANCED': 'true',
        'FIND_BY_NAME': 'true',
        'INDIVIDUAL_NAME': f"{first_name} {last_name}",
        'resultsPerPage': '10'
    }

    response = requests.get(search_url, params=search_params)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    search_results = soup.find_all('a', {'class': 'individual-summary'})

    for result in search_results:
        if first_name.lower() in result.text.lower() and last_name.lower() in result.text.lower():
            adviser_url = "https://adviserinfo.sec.gov" + result['href']
            return get_adviser_info(adviser_url)

    return None


def get_adviser_info(adviser_url):
    response = requests.get(adviser_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract specific information using the new HTML structure provided
        name = soup.find('span', class_='text-lg sm:text-sm font-semibold').text.strip()
        firm = soup.find('span', {'class': 'firmName'}).text.strip()
        crd_number = soup.find('span', {'class': 'crdNumber'}).text.strip()

        return {
            'Name': name,
            'Firm': firm,
            'CRD Number': crd_number
        }
    else:
        return None


# Example usage
first_name = 'Kelly'
last_name = 'Demers'
info = search_adviser_by_name(first_name, last_name)
if info:
    print(info)
else:
    print("Failed to retrieve adviser information.")