from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException

import time

# driver = webdriver.Chrome(service=service, options=options)
driver = webdriver.Remote(
    "http://localhost:4444/wd/hub",
    desired_capabilities=DesiredCapabilities.CHROME,
)
driver.maximize_window()
driver.implicitly_wait(10)

start_url = "https://www.lavoro.gov.it/"

all_data = []

keywords = ['big data', 'data warehouse', 'data lake', 'data science', 'data mining', 'data privacy', 'open data',
            'data governance', 'data literacy', 'data', 'biometric', 'analisi biometrica',
            'machine learning', 'apprendimento automatico', 'algoritm', 'calcolo', 'punteggio', 'valutazione',
            'monitoraggi','predittiv', 'cloud', 'statistic', 'reti neurali', 'rete neurale', 'neural network',
            'apprendimento profondo', 'deep learning', 'ranking', 'classificazione', 'apprendimento supervisionato',
            'apprendimento non supervisionato', 'software', 'numeric', 'rango', 'ranghi', 'rank', "Elaborazione del linguaggio naturale",
            'natural language processing', 'NLP', 'graduazione', 'transformer', 'GPT', 'Bard', 'Copilot', 'Gemini', 'DALL-E',
            'automa', 'internet delle cose', 'intelligenza artificiale']

for word in keywords:
    driver.get(start_url)

    time.sleep(5)

    # Accept cookies.
    try:
        driver.find_element(By.CSS_SELECTOR, "button.agree-button").click()
    except NoSuchElementException:
        pass

    print(f"Search: {word}.")
    searchbar = driver.find_element(By.ID, "search-input")
    searchbar.send_keys(word)
    searchbar.send_keys(Keys.ENTER)
    
    while True:
        time.sleep(10)

        next = driver.find_element(By.CSS_SELECTOR, "a[rel='next']")
        # Check if next button is disabled (no more data).
        if next.get_attribute("aria-hidden") is not None:
            print("No more data.")
            break
        next = next.get_attribute("href")
        print(f"Next page: {next}.")

        driver.get(next)
            
driver.quit()