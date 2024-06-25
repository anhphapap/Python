import pandas as pd
from bs4 import BeautifulSoup
import requests

table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table,"html.parser")
tRow = table_bs.find_all('tr')
for i,r in enumerate(tRow):
    print("row",i)
    c = r.find_all('td')
    for j,cell in enumerate(c):
        print('column ',j,'cell ',cell)

# Scrape all links in this web "http://www.ibm.com"
url = "http://www.ibm.com"
data = requests.get(url).text
soup = BeautifulSoup(data, "html.parser")
for i in soup.find_all('a', href = True):
    print(i['href'])
# Scrape all images
for i in soup.find_all('img'):
    print(i["src"])

