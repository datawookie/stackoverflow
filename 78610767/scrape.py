from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

url = "https://new.abb.com/products/SK615502-D"

options = webdriver.ChromeOptions()
# * Use local Chrome.
# driver = webdriver.Chrome(options=options)
# * Use remote Chrome in Docker container.
driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME, options=options)

wait = WebDriverWait(driver, 10)

driver.get(url)

# Find element enclosing the shadow root DOM.
#
root = driver.find_element(By.CSS_SELECTOR, "pis-products-details-attribute-groups")

# Extract the shadow root content.
#
shadow_root = driver.execute_script("return arguments[0].shadowRoot", root)
print(shadow_root)

for table in shadow_root.find_elements(By.CSS_SELECTOR, ".ext-attr-group .ext-attr-group-inner"):
    title = table.find_element(By.CSS_SELECTOR, "h4")
    print("====================================================")
    print("🟦 " + title.text)
    for row in table.find_elements(By.CSS_SELECTOR, ".ext-attr-group-content > div"):
        key = row.find_element(By.CSS_SELECTOR, ".col-md-4")
        value = row.find_element(By.CSS_SELECTOR, ".col-md-8")
        print(str(key.text) + " " + str(value.text))
