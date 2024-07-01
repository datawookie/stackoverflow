from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", options=options)


def wait_and_click(driver, by, value, retries=3):
    for _ in range(retries):
        try:
            element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((by, value)))
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()
            return True
        except Exception as e:
            print(f"Error clicking element {value}: {e}")
            time.sleep(2)
    return False


driver.get("https://www.nfrc.co.uk/search-members")

wait_and_click(driver, By.LINK_TEXT, "Search for a roofing contractor now")

wait_and_click(driver, By.CLASS_NAME, "sfDropdownList")

wait_and_click(driver, By.XPATH, '//option[@value="CONTRACTOR_ADVANCED_DOMESTIC_PROPERTY_VIEW"]')

wait_and_click(driver, By.ID, "MainContent_C001_btnSearch")

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".search_results")))

while True:
    index = 0

    # Can't just iterate over list of elements because when return to page these elements are stale.
    #
    while True:
        results = driver.find_elements(By.CSS_SELECTOR, "h3 > a")

        try:
            results[index].click()
        except IndexError:
            # Exhausted all results on page.
            break

        try:
            link = driver.find_element(
                By.CSS_SELECTOR, "#ctl00_MainContent_C004_radListView_ctrl0_tr4 td.details_item > a"
            )
            print(link.get_attribute("href"))
        except NoSuchElementException:
            # No URL on contractor page.
            pass

        # Return to search results.
        driver.back()

        index += 1

    paginate = driver.find_elements(By.CSS_SELECTOR, "#ctl00_MainContent_C001_radListView_radDataPager1 a")

    for next in range(len(paginate)):
        page = paginate[next]
        if page.get_attribute("onclick") == "return false;":
            print("⏩ Move to next page!")
            paginate[next + 1].click()
            break

driver.close()
