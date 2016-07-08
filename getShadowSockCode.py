#-*- coding: utf-8 -*-
#getShadowSockCode
#create on '16-6-3'
#! /usr/bin/env python3
__author__ = 'valiant'

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re



try:
    html = urlopen("http://www.ishadowsocks.net/")
    beauty = BeautifulSoup(html, "lxml")
    lines = beauty.find("section", {"id": "free"}).findAll("div", {"class": "col-lg-4 text-center"})
    for line in lines:
        print(line.get_text())
except (HTTPError, ConnectionError) as e:
    print(e)


pattern = re.compile("iframe")
pattern1 = re.compile("\"(.+?)\"")
try:
    html = urlopen("http://www.shadowsocks.asia/mianfei/10.html")
    beauty = BeautifulSoup(html, "lxml")
    lines = beauty.findAll("div", {"class" : "codediv"})
    for line in lines:
        item = line.find("textarea", {"class":"codetextarea"})
        if item is not None:
            result = item.get_text()
            if result is not None:
                if pattern.findall(result):
                    url = pattern1.findall(result)
                    if url is not None:
                        php = urlopen(url[0])
                        obj = BeautifulSoup(php, "lxml")
                        result = obj.find("body")
                        print(result.get_text())
                        print("\n")
                else:
                    print(result)
except (HTTPError, ConnectionError) as e:
    print(e)
