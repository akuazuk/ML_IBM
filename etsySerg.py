#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
url1 = "https://www.proartsuppliesusa.com/shop/11241211/watercolors-set"
list2 = []
html_doc = requests.get(url1)
soup = BeautifulSoup(html_doc.text, 'html.parser')
discription = soup.find_all(class_=["title", "price"])
for price in discription:
    str1=price.text.replace('\n','')
    str2=str1.rstrip(' ')
    list2.append(str2.lstrip(' '))

print(list2)

