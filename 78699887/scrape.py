from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pickle
import os
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # headless mode
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("enable-automation")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.maximize_window()
    return driver
def load_cookies(driver, url):
    # Create the "cookies" directory if it does not exist
    cookies_dir = "cookies"
    if not os.path.exists(cookies_dir):
        os.makedirs(cookies_dir)

    # Specify the full path to the cookie file
    cookies_file = os.path.join(cookies_dir, "bwin.pkl")

    driver.get(url)
    if os.path.exists(cookies_file):
        with open(cookies_file, "rb") as cookiesfile:
            cookies = pickle.load(cookiesfile)
            for cookie in cookies:
                driver.add_cookie(cookie)
            driver.refresh()
    else:
        close_popups(driver)
        with open(cookies_file, "wb") as cookiesfile:
            pickle.dump(driver.get_cookies(), cookiesfile)
def close_popups(driver):
    try:
        print("Attempting to close promotion popup")
        popup_promotion = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#messages-with-overlay > div > vn-content-message > div > span')))
        popup_promotion.click()
    except Exception as e:
        print(f"No promotion popup found: {e}")

    try:
        print("Attempting to close cookie banner")
        banner_cookie = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#onetrust-accept-btn-handler')))
        banner_cookie.click()
    except Exception as e:
        print(f"No cookie banner found: {e}")
def get_page_source(url):
    driver = setup_driver()
    load_cookies(driver, url)

    try:
        print("Waiting for ms-event-group element")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'ms-event-group')))
    except Exception as e:
        print(f"Loading timeout or error: {e}")

    try:
        print("Waiting for ms-league-header element")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'ms-league-header')))
    except Exception as e:
        print(f"Alternative loading timeout or error: {e}")

    page_source = driver.page_source
    driver.quit()
    return page_source

def remove_duplicate_characters(list):
    return [elem[0] if len(elem) == 2 and elem[0] == elem[1] else elem for elem in list]

def scrape_bwin():
    url = "https://sports.bwin.it/it/sports/live/tennis-5"
    print("Fetching page source")
    page_source = get_page_source(url)
    soup = BeautifulSoup(page_source, 'html.parser')

    tournaments_list = []
    players_list = []
    odds_player1_list = []
    odds_player2_list = []
    sets_list = []
    games_list = []
    points_player1_list = []
    points_player2_list = []
    event_status_list = []
    current_set_list = []

    tournaments = soup.select('ms-event-group')

    for tournament in tournaments:
        tournament_name = tournament.select_one('ms-league-header .title span')
        if tournament_name:
            tournament_name = tournament_name.text.strip()
        else:
            continue

        events = tournament.select('ms-event')
        for event in events:
            event_status_elem = event.select_one('ms-event-detail > div > ms-event-info > i.live-icon')
            event_status = "Live" if event_status_elem else "Non live"

            if event_status != "Live":
                continue

            players = [elem.text.strip() for elem in event.select('ms-event-name ms-inline-tooltip div div div div')]

            odds_elements = event.select('ms-option-group:nth-child(1) ms-option')
            odds = [float(elem.text.strip()) for elem in odds_elements[:2] if
                     elem.text.strip().replace('.', '', 1).isdigit()]

            if len(odds) < 2:
                continue

            sets = remove_duplicate_characters(
                [elem.text.strip() for elem in event.select('ms-set-game-scoreboard div.column.sets > div')])
            games = remove_duplicate_characters(
                [elem.text.strip() for elem in event.select('ms-set-game-scoreboard div.column.games.divider > div')])
            points_elements = event.select('ms-set-game-scoreboard div.column.points > div:nth-child(1) > div > div')
            points = [elem.text.strip() for elem in points_elements]

            if len(points) == 2:
                points_player1 = points[0]
                points_player2 = points[1]
            else:
                points_player1 = "N/A"
                points_player2 = "N/A"

            current_set_elem = event.select_one(
                'ms-event-detail > div > ms-event-info > div > ms-event-timer > ms-live-timer')
            current_set = current_set_elem.text.strip() if current_set_elem else "N/A"

            tournaments_list.append(tournament_name)
            players_list.append(players)
            odds_player1_list.append(odds[0])
            odds_player2_list.append(odds[1])
            sets_list.append(sets)
            games_list.append(games)
            points_player1_list.append(points_player1)
            points_player2_list.append(points_player2)
            event_status_list.append(event_status)
            current_set_list.append(current_set)

    df = pd.DataFrame({
        'Tournaments': tournaments_list,
        'Players': players_list,
        'Odds Player 1': odds_player1_list,
        'Odds Player 2': odds_player2_list,
        'Sets': sets_list,
        'Games': games_list,
        'Points Player 1': points_player1_list,
        'Points Player 2': points_player2_list,
        'Event Status': event_status_list,
        'Current Set': current_set_list
    })

    df.to_csv('live tennis matches.csv', index=False)
    print(df)

scrape_bwin()