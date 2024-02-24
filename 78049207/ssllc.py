from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions

import traceback
import time
import logging

logging.basicConfig(
  level=logging.DEBUG,
  format='%(asctime)s [%(levelname)7s] %(message)s',
)
logging.getLogger("selenium").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

BASE_URL = "https://www.ssllc.com"

SEARCH_QUERIES = [
    'Unused Sartorius 1000 Liter BIOSTAT CultiBag STR Single Use Bioreactor',
    '3 x V5/XCell Repigen Next Gen ATF controllers',
    'InSite Integrity Tester'
]

RESULTS = []

options = ChromeOptions()
# options.add_argument('--headless')

# Don't instantiate browser inside loop. Once is enough!
with Chrome(options=options) as driver:
    # Just open the base URL once too.
    driver.get(BASE_URL)
    try:
        for search_query in SEARCH_QUERIES:
            # logging.info(f"* Search term: {search_query}")
            # search_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((
            #     By.CSS_SELECTOR,
            #     ".search-row input[type=text]"
            # )))
            # logging.debug("- Clear existing search term.")
            # search_input.clear()
            # time.sleep(5)
            # logging.debug("- Insert search term.")
            # search_input.send_keys(search_query)
            # time.sleep(10)
            # logging.debug("- Run search.")
            # search_input.send_keys(Keys.RETURN)

            query_url = BASE_URL+"/search/?query='"+search_query+"'"
            driver.get(query_url)

            logging.debug("- Wait for results to load.")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                By.CSS_SELECTOR,
                ".ais-Hits > ul.ais-Hits-list"
            )))

            logging.debug("- Extract results.")
            search_results = driver.find_elements(
                By.CSS_SELECTOR,
                ".ais-Hits > ul.ais-Hits-list > li"
            )

            results = []

            if search_results:
                logging.info(f"✅ Search results ({len(search_results)} items).")
                for result in search_results:

                    # Get the link to the search result

                    #result_link = result.find_element(By.TAG_NAME, 'a').get_attribute('href')

                    #logging.info(f"{result.text.strip()} - {result_link}")
                    results.append(result.text.strip())
            else:

                logging.warning(f"🚨 No search results found for '{search_query}'")

            time.sleep(20)

            RESULTS.append({
                "search": search_query,
                "results": results
            })

            time.sleep(60)

    except Exception as e:
        logging.error("An error occurred:"+str(e))
        logging.error(traceback.format_exc())
