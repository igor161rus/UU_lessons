import re
import time
import datetime

import pandas as pd
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver

url = 'https://coinmarketcap.com/ru/'


def get_driver():
    driver = webdriver.Chrome()
    driver.get(url)

    scroll_pause_time = 3

    i = 0
    while i < 15:
        driver.execute_script("window.scrollBy(0, window.innerHeight)")
        time.sleep(scroll_pause_time)
        i += 1

    return driver.page_source


def write_cmc_top():
    driver = get_driver()

    soup = BeautifulSoup(driver, features='lxml')
    # <span class="SummaryHeader_normal-des__hhWcs" style="display: inline-block; margin-inline-end: var(--c-space-50);"><p color="neutral6" font-size="1" data-sensors-click="true" class="sc-4984dd93-0 sc-aec1c3fa-0 iSIYjT" style="display: inline;">Глобальная капитализация рынка криптовалют составляет <span color="neutral6" font-weight="semibold" font-size="1" data-sensors-click="true" class="sc-4984dd93-0 sc-aec1c3fa-0 fyTlPK">₽246.18T</span>., Снижение за предыдущий день: <span class="sc-f1e838b2-0 dRLonq" style="color: var(--down-color); padding: 0px; border-radius: 8px; font-weight: 600;"><span class="icon-Caret-down"></span>1.58%</span>.</p></span>
    cap_global_text = soup.find_all('span', {'class': 'SummaryHeader_normal-des__hhWcs'})
    match = re.findall(r'(\d*\.\d{2})', cap_global_text[0].text)
    # print(cap_global_text[0].text, ' - ', match[0])
    cap_global = float(match[0])

    table = soup.find_all('table')
    df = pd.read_html(str(table))[0]

    mc = 'Рыночная капитализация'
    res_df = df[['Наименование', mc]]
    res_df = res_df.rename(columns={'Наименование': 'Name'})
    res_df['MC'] = df[mc]
    res_df[mc] = res_df[mc].str.replace(r'^.\d{1,3}\.\d{1,2}.{2}|^.\d{1,3}.{2}', '', regex=True)
    res_df[mc] = res_df[mc].str.replace(r'\D+', '', regex=True).astype('int64')
    res_df['MC'] = res_df['MC'].str.replace(r'^.\d{1,3}\.\d{1,2}.{2}|^.\d{1,3}.{2}', '', regex=True)
    res_df['MP'] = round((res_df[mc] / cap_global ** 6) * 100, 2).astype(str) + '%'
    del res_df[mc]
    # print(res_df)
    res_df.to_csv(datetime.datetime.now().strftime('%H.%M %d.%m.%Y') + '.csv')


write_cmc_top()
