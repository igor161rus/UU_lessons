import re
import time
import csv
import datetime

from bs4 import BeautifulSoup
import requests
import lxml
from selenium import webdriver

url = 'https://coinmarketcap.com/ru/'


def get_driver():
    driver = webdriver.Chrome()
    driver.get(url)

    SCROLL_PAUSE_TIME = 3

    i = 0
    while i < 15:
        driver.execute_script("window.scrollBy(0, window.innerHeight)")
        time.sleep(SCROLL_PAUSE_TIME)
        i += 1

    return driver.page_source


driver = get_driver()

# response = requests.get(driver).text

soup = BeautifulSoup(driver, features='lxml')
# <span class="SummaryHeader_normal-des__hhWcs" style="display: inline-block; margin-inline-end: var(--c-space-50);"><p color="neutral6" font-size="1" data-sensors-click="true" class="sc-4984dd93-0 sc-aec1c3fa-0 iSIYjT" style="display: inline;">Глобальная капитализация рынка криптовалют составляет <span color="neutral6" font-weight="semibold" font-size="1" data-sensors-click="true" class="sc-4984dd93-0 sc-aec1c3fa-0 fyTlPK">₽246.18T</span>., Снижение за предыдущий день: <span class="sc-f1e838b2-0 dRLonq" style="color: var(--down-color); padding: 0px; border-radius: 8px; font-weight: 600;"><span class="icon-Caret-down"></span>1.58%</span>.</p></span>
cap_global_text = soup.find_all('span', {'class': 'SummaryHeader_normal-des__hhWcs'})

match = re.findall(r'(\d*\.\d{2})', cap_global_text[0].text)
cap_global = match[0]
data_list = []
print(cap_global_text[0].text, ' - ', match[0])
for i in soup.findAll('tr')[1:]:
    name = i.findAll('td')[2].text.replace(' ', '_')
    # price = i.findAll('td')[4].text
    cap = i.findAll('td')[7].text
    match = re.findall(r'[^₽][^₽]*', cap)
    cap_percent = round((int(match[1].replace(',', '')) / (float(cap_global) * 10 ** 12)) * 100, 2)
    # name = name.strip()
    # price = price.strip()
    # cap = cap.strip()
    data_list.append([name, match[1], cap_percent])
    print(name, match[1], cap_percent, '%')

headers = ['Name', 'MC', 'MP']
with open(datetime.datetime.now().strftime('%H.%M %d.%m.%Y') + '.csv', 'w', newline='') as out_csv:
    csvwriter = csv.writer(out_csv)
    csvwriter.writerow(headers)
    csvwriter.writerows(data_list)



def write_cmc_top():
    pass
