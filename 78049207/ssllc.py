from selenium.webdriver import Chrome

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options as ChromeOptions



# Define the base URL of the website

base_url = 'https://www.ssllc.com'

search_bar='#page-top > div > div > div > div:nth-child(1) > input[type=text]' #CSS_SELECTOR

items = '#gatsby-focus-wrapper > div.root > div > div > div > div.medium-8.columns.main-content > div.ais-Hits > ul '



# Define the list of search queries

search_queries = [
 'Unused+Sartorius+1000+Liter+BIOSTAT+CultiBag+STR+Single+Use+Bioreactor',


'3+x+V5/XCell+Repigen+Next+Gen+ATF+controllers',

'InSite+Integrity+Tester'

]



# Configure ChromeOptions

options = ChromeOptions()

options.add_argument('--headless')  # Optional: Run Chrome in headless mode for faster execution



try:

for search_query in search_queries:

    # Initialize Chrome WebDriver for each search

    with Chrome(options=options) as driver:

        # Load the website

        driver.get(base_url)



        # Find the search input field and enter the query

        search_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, search_bar)))

        search_input.clear()

        search_input.send_keys(search_query)

        search_input.send_keys(Keys.RETURN)



        # Wait for the search results to load

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, items )))



        # Extract and print search results

        search_results = driver.find_elements(By.CSS_SELECTOR, items )

        if search_results:

            print(f"Search results for '{search_query}':")

            for result in search_results:

                # Get the link to the search result

                #result_link = result.find_element(By.TAG_NAME, 'a').get_attribute('href')

                #print(f"{result.text.strip()} - {result_link}")

                print(result.text.strip())

                print()

        else:

            print(f"No search results found for '{search_query}'")

except Exception as e:

print("An error occurred:", e)
