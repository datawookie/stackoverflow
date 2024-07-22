from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

# from selenium.webdriver.edge.options import Options
from selenium.webdriver.chrome.options import Options
import time

# service = Service("C:/Users/PERSONAL/Downloads/msedgedriver.exe")
# driver = webdriver.Edge(service=service, options=edge_options)

DRIVER_PATH = "/usr/bin/chromedriver"

options = Options()

service = Service(executable_path=DRIVER_PATH)

driver = webdriver.Chrome(service=service, options=options)

# # driver.get("https://www.bbva.com.co/personas/productos/inversion/fondos/pais.html")
driver.get(
    "https://bbva-cells-files.s3.amazonaws.com/cells/apps/bbva_es_ficha_global_am_cells/bbva_ficha_global_am_cells_co/master/cellsapp/prod/vulcanize/index.html#!/CCAPAISCB"
)

# # # iframe = driver.find_element(By.XPATH, "//*[@id = 'content-iframe_copy']")
# # iframe = driver.find_element(By.CSS_SELECTOR, "#content-iframe_copy")

# # with open("page.html", "wt") as file:
# #     file.write(driver.page_source)

# # print(iframe)
# # url = iframe.get_attribute("src")
# # print(url)

# # driver.get(url)

time.sleep(5)

shadow_host = driver.find_element(By.CSS_SELECTOR, "fichaco-page")
print(shadow_host)
shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
print(shadow_root)

# element_inside_shadow_dom = driver.execute_script('return arguments[0].querySelector(".liquidativo-rentabilidad")', shadow_root)
# print(element_inside_shadow_dom)

price = driver.execute_script(
    """
    var shadowHost = document.querySelector('fichaco-page');
    var shadowRoot = shadowHost.shadowRoot;
    return shadowRoot.querySelector('.liquidativo-rentabilidad').textContent;
"""
)

print(price)

# # print("Cambiamos el foco el IFRAME")
# # driver.switch_to.frame(iframe)

# # print("Obtener el dato")
# # dato = driver.find_elements(By.TAG_NAME, "g")
# # print(dato)

# # pesos = driver.find_element(By.CSS_SELECTOR, "body")

# # with open("iframe.html", "wt") as file:
# #     file.write(pesos.get_attribute('innerHTML'))
# with open("iframe.html", "wt") as file:
#     file.write(driver.page_source)

# pesos = driver.find_element(By.CSS_SELECTOR, ".liquidativo-rentabilidad")

driver.quit()

# import time
# from playwright.sync_api import sync_playwright, TimeoutError
# from playwright._impl._errors import Error as PlaywrightError

# # URL = "https://www.bbva.com.co/personas/productos/inversion/fondos/pais.html"
# URL = "https://bbva-cells-files.s3.amazonaws.com/cells/apps/bbva_es_ficha_global_am_cells/bbva_ficha_global_am_cells_co/master/cellsapp/prod/vulcanize/index.html#!/CCAPAISCB"

# playwright = sync_playwright().start()
# browser = playwright.chromium.launch(headless=False, slow_mo=2000)
# context = browser.new_context(
#     viewport={"width": 1280, "height": 900}
# )

# page = context.new_page()

# page.goto(URL)

# time.sleep(5)

# # Get HTML page content.
# #
# html = page.content()

# with open("page.html", "wt") as file:
#     file.write(html)

# page.close()
