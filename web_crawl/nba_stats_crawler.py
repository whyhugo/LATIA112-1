import requests as rq
import pandas as pd
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from lxml import etree
import time

url = 'https://www.nba.com/stats/players/traditional'
driver = webdriver.Chrome('/programing/swiftx/chromedriver-win64/chromedriver.exe')
html = driver.get(url)
sp = soup(driver.page_source, 'html.parser')

def get_column_name():
    data_column_name = []
    sp = soup(driver.page_source, 'html.parser')
    th_tags = sp.find('tr', class_='Crom_headers__mzI_m').find_all('th')
    for th_tag in th_tags:
        data_column_name.append(th_tag.text)
    data_column_name = data_column_name[1:30]
    return data_column_name

def click_next_page_button():
    time.sleep(3)
    element = driver.find_element('xpath', '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[5]/button[2]')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(2)

def get_data():
    data = []
    row = []
    count = 0
    sp = soup(driver.page_source, 'html.parser')
    tr_tags = sp.find('tbody', class_='Crom_body__UYOcU').find_all('tr')
    for tr_tag in tr_tags:
        td_tags = tr_tag.find_all('td')
        for td_tag in td_tags:
            row.append(td_tag.text)
            count += 1
            if count % 30 == 0:
                data.append(row[1:])
                row = []
    return data

try:
    df_list = []
    sp = soup(driver.page_source, 'html.parser')
    total_row = sp.find('div', class_='Pagination_content__f2at7 Crom_cromSetting__Tqtiq').find('div').text[:-5]
    while True:
        print('New Page!')
        time.sleep(2)
        df_list.extend(get_data())
        if len(df_list) == int(total_row):
            print('This is the last page ( •̀ ω •́ )✧')
            break
        else:
            click_next_page_button()
except:
    print('Something went wrong. QAQ')

df = pd.DataFrame(df_list, columns=get_column_name())
df.to_csv('nba_stats.csv', index=False, encoding='utf-8')

driver.quit()