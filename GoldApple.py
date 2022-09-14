#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from bs4 import BeautifulSoup
import re
from re import sub
from datetime import datetime
from selenium import webdriver
import time
from time import sleep
import requests
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import warnings
warnings.filterwarnings("ignore")


# In[ ]:


makijazh = 'https://goldapple.ru/makijazh'
uhod = 'https://goldapple.ru/uhod'
volosy = 'https://goldapple.ru/volosy'
parfjumerija = 'https://goldapple.ru/parfjumerija'
zdorove_apteka = 'https://goldapple.ru/zdorov-e-i-apteka'
sexual_wellness = 'https://goldapple.ru/sexual-wellness'
azija = 'https://goldapple.ru/azija'
organika = 'https://goldapple.ru/organika'
muzhchina = 'https://goldapple.ru/dlja-muzhchin'
dlja_detej = 'https://goldapple.ru/dlja-detej'
tehnika = 'https://goldapple.ru/tehnika'
dlja_doma = 'https://goldapple.ru/dlja-doma'
odezhda = 'https://goldapple.ru/odezhda-i-aksessuary'
beljo = 'https://goldapple.ru/nizhnee-bel-jo'
ukrashenija = 'https://goldapple.ru/ukrashenija'
trevel = 'https://goldapple.ru/trevel-formaty'
zhivotnyh = 'https://goldapple.ru/tovary-dlja-zhivotnyh'
sale = 'https://goldapple.ru/sale-july-ru'


# In[ ]:


driver = webdriver.Chrome(executable_path='./chromedriver.exe')


# In[ ]:


def parser(url):
    data = []

    for page in range(1, 4):
        print(page)
    
        PRODUCT_URL = url+f"?p={page}"
    
        driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver.get(PRODUCT_URL)
        sleep(3)
        html = driver.page_source
        soup = BeautifulSoup(html, "lxml")
    
        items = soup.find_all('div', class_='product details product-item-details')

        for item in items:
            categories = item.find("div", class_="product-item-category-title").get_text().strip()
            brand_names = item.find("span", class_="catalog-brand-name-span").get_text()
            product_names = item.find("span", class_="catalog-product-name-span").get_text()
            try:
                prices = item.find("span", class_="price").get_text()
                prices = int(sub("[^0-9]", "", prices))
            except:
                print('-')
            new_price = item.find("span", class_="price-wrapper")
            old_price = item.find("span", class_="old-price sly-old-price")
            update_date=datetime.now()
    
            data.append([categories, brand_names, product_names, old_price, new_price, prices, update_date])

        driver.close()
        driver.quit()
        
        header = ['categories', 'brand_names', 'product_names', 'old_price', 'new_price', 'prices', 'update_date']
        df = pd.DataFrame(data, columns=header)
        df['old_price'] =  df['old_price'].apply(lambda x: re.sub(r'[^\d]+', '', str(x)))
        df['new_price'] =  df['new_price'].apply(lambda x: re.sub(r'[^\d]+', '', str(x)))
        df['prices'] =  df['prices'].apply(lambda x: re.sub(r'[^\d]+', '', str(x)))
        df['current_price'] = df[['new_price','prices']].max(axis = 1)
        df['current_price'] = df['current_price'].astype('int32')
        del df['prices'], df['new_price']
        df_new = df[['categories', 'brand_names', 'product_names', 'old_price', 'current_price', 'update_date']]
        if items
    return df_new


# In[ ]:


makeup = []
care = []
hair = []
parfume = []
health = []
sex_wellness = []
asia = []
organic = []
men = []
kids = []
tech = []
home = []
clothes = []
underwear = []
jewls = []
travel = []
pets = []

makeup = parser(makijazh)
care = parser(uhod)
hair = parser(volosy)
parfume = parser(parfjumerija)
health = parser(zdorove_apteka)
sex_wellness = parser(sexual_wellness)
asia = parser(azija)
organic = parser(organika)
men = parser(muzhchina)
kids = parser(dlja_detej)
tech = parser(tehnika)
home = parser(dlja_doma)
clothes = parser(odezhda)
underwear = parser(beljo)
jewls = parser(ukrashenija)
travel = parser(trevel)
pets = parser(zhivotnyh)
sale_july = parser(sale)


# In[ ]:


from pandas.io.excel import ExcelWriter

makeup.to_excel('/Users/HomeNote/Desktop/parser_ga.xlsx', sheet_name='makeup')

with ExcelWriter('/Users/HomeNote/Desktop/parser_ga.xlsx', engine="openpyxl", mode="a") as writer: 
    care.to_excel(writer, sheet_name="care")
    hair.to_excel(writer, sheet_name="hair")
    parfume.to_excel(writer, sheet_name="parfume")
    health.to_excel(writer, sheet_name="health")
    sex_wellness.to_excel(writer, sheet_name="sex_wellness")
    asia.to_excel(writer, sheet_name="asia")
    organic.to_excel(writer, sheet_name="organic")
    men.to_excel(writer, sheet_name="men")
    kids.to_excel(writer, sheet_name="kids")
    tech.to_excel(writer, sheet_name="tech")
    home.to_excel(writer, sheet_name="home")
    underwear.to_excel(writer, sheet_name="underwear")
    clothes.to_excel(writer, sheet_name="clothes")
    jewls.to_excel(writer, sheet_name="jewls")
    travel.to_excel(writer, sheet_name="travel")
    pets.to_excel(writer, sheet_name="pets")
    sale_july.to_excel(writer, sheet_name="sale_july")
    

