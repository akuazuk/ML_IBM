#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
url1 = "https://www.saltlakevalleychryslerdodgeramjeep.com/new-vehicles/grand-cherokee/#action=im_ajax_call&perform=get_results&page=1&model%5B%5D=Grand+Cherokee+L"
list2 = []
html_doc = requests.get(url1)
soup = BeautifulSoup(html_doc.text, 'html.parser')
discription2 = soup.find_all(class_="vehicle-title clearfix")

#discription2 = soup.find("a", class_="save-things save-things-save") ["data-title"]
print (discription2)




