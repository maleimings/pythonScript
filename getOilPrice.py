#-*- coding: UTF-8 -*-
#getOilPrice
#create on '16-6-8'
__author__ = 'valiant'
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

site = "http://www.bitauto.com/youjia/xian/"

html = urlopen(site)

soup = BeautifulSoup(html, "lxml")

items = soup.find("ul",{"id": "car_tab_ul2"}).findAll("span", class_=re.compile("(oilNum|todayPrice)"))

for item in items:
    print(item.get_text())
