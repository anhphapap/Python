import pandas as pd
import requests
import sqlite3
from bs4 import BeautifulSoup

movie_db = "Movies.db"
movie_csv = "Top50films.csv"
counter = 0
url = "https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films"
df = pd.DataFrame(columns=["Average Rank","Film","Year"])
table_name = "Top_50"

html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

tables = soup.find_all("tbody")
rows = tables[0].find_all("tr")

for x in rows:
    if counter < 50: 
        col = x.find_all("td")
        if len(col) > 2:
            dict = {"Average Rank":col[0].contents[0],
            "Film":col[1].contents[0],
            "Year":col[2].contents[0]}
            df = pd.concat([df,pd.DataFrame(dict,index=[0])],ignore_index=True)
            counter += 1
    else:
        break

print(df)

df.to_csv(movie_csv)

conn = sqlite3.connect(movie_db)
df.to_sql(table_name, conn,if_exists="replace", index=False)
conn.close()

    