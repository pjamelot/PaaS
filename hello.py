
#https://www.youtube.com/watch?v=Bg9r_yLk7VY&t=66s 

import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.fr/Nouvel-Apple-pouces-Wi-Fi-128Go/dp/B07XSCLLV7/ref=sr_1_1_sspa?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3N33YE5RUE61V&keywords=ipad+128go&qid=1573511376&sprefix=ipad+128G%2Caps%2C295&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVUJGR1FLWjFIVURaJmVuY3J5cHRlZElkPUEwOTAwMTI3MUhWMU83V0o4UFJSUCZlbmNyeXB0ZWRBZElkPUEwNzE0MTE4MklBVEdZMFpETk85NSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

headers = { "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')


#print(soup.prettify())
title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
converted_price = price[0:5]

print(converted_price)
print(title.strip())