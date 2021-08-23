#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
url1 = "https://www.etsy.com/market/nevskaya_palitra?ref=pagination"
list2 = []
html_doc = requests.get(url1)
soup = BeautifulSoup(html_doc.text, 'html.parser')
discription = soup.find_all(class_=["wt-mb-xs-0 wt-text-truncate wt-text-caption listing-title-experimental-style", "currency-value"])
for price in discription:
    str1=price.text.replace('\n','')
    str2=str1.rstrip(' ')
    list2.append(str2.lstrip(' '))

print(list2)

