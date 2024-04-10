import re
import time

from bs4 import BeautifulSoup
import requests
import lxml
from selenium import webdriver

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC

# import pandas as pd

url = 'https://coinmarketcap.com/ru/'


def get_driver():
    driver = webdriver.Chrome()
    driver.get(url)

    SCROLL_PAUSE_TIME = 3
    # WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "div.cmc-cookie-policy-banner__close"))).click()
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button/b[text()='No, thanks']"))).click()
    # Get scroll height
    # last_height = driver.execute_script("return document.body.scrollHeight")
    #
    # while True:
    #     # Scroll down to bottom
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    i = 0
    while i < 15:
        driver.execute_script("window.scrollBy(0, window.innerHeight)")
        time.sleep(SCROLL_PAUSE_TIME)
        i += 1

    # Wait to load page
    # time.sleep(SCROLL_PAUSE_TIME)
    #
    # # Calculate new scroll height and compare with last scroll height
    # new_height = driver.execute_script("return document.body.scrollHeight")
    # if new_height == last_height:
    #     break
    # last_height = new_height
    return driver.page_source


driver = get_driver()

# response = requests.get(driver).text

soup = BeautifulSoup(driver, features='lxml')
# <span class="SummaryHeader_normal-des__hhWcs" style="display: inline-block; margin-inline-end: var(--c-space-50);"><p color="neutral6" font-size="1" data-sensors-click="true" class="sc-4984dd93-0 sc-aec1c3fa-0 iSIYjT" style="display: inline;">Глобальная капитализация рынка криптовалют составляет <span color="neutral6" font-weight="semibold" font-size="1" data-sensors-click="true" class="sc-4984dd93-0 sc-aec1c3fa-0 fyTlPK">₽246.18T</span>., Снижение за предыдущий день: <span class="sc-f1e838b2-0 dRLonq" style="color: var(--down-color); padding: 0px; border-radius: 8px; font-weight: 600;"><span class="icon-Caret-down"></span>1.58%</span>.</p></span>
cap_global_text = soup.find_all('span', {'class': 'SummaryHeader_normal-des__hhWcs'})

match = re.findall(r'(\d*\.\d{2})', cap_global_text[0].text)
cap_global = match[0]
print(cap_global_text[0].text, ' - ', match[0])
for i in soup.findAll('tr')[1:]:
    name = i.findAll('td')[2].text
    # price = i.findAll('td')[4].text
    cap = i.findAll('td')[7].text
    match = re.findall(r'[^₽][^₽]*', cap)
    cap_percent = round((int(match[1].replace(',', '')) / (float(cap_global) * 10**12)) * 100, 2)
    # name = name.strip()
    # price = price.strip()
    # cap = cap.strip()

    print(name, match[1], cap_percent, '%')


# pd.set_option('display.max_columns', None)
# aa = pd.read_html(url)
# # aa.to_csv('cmc.csv')
# print(aa)


def write_cmc_top():
    pass
