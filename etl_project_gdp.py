import pandas as pd 
from bs4 import BeautifulSoup
import requests
import sqlite3
import numpy 
from datetime import datetime

url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
table_attribs = ["Country","GDP_USD_millions"]
db_name = "World_Economies.db"
table_name = "Countries_by_GDP"
csv_path = "Countries_by_GDP.csv"

def extract(url, table_attribs):
    page = requests.get(url).text
    data = BeautifulSoup(page,"html.parser")
    df = pd.DataFrame(columns=table_attribs)
    tables = data.find_all("tbody")
    rows = tables[2].find_all("tr")
    for x in rows:
        col = x.find_all("td")
        if len(col) != 0:
            if col[0].find('a') is not None and '—' not in col[2]:
                data_dict = {"Country":col[0].a.contents[0],
                             "GDP_USD_millions": col[2].contents[0]}
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df,df1], ignore_index=True)
    return df

def transform(df):
    list = df["GDP_USD_millions"].tolist()
    list = [float(''.join(x.split(','))) for x in list]
    list = [numpy.round(x/1000,2) for x in list]
    df["GDP_USD_millions"] = list
    df = df.rename(columns = {"GDP_USD_millions":"GDP_USD_billions"})
    return df

def load_to_csv(df, csv_path):
    df.to_csv(csv_path)

def load_to_db(df, sql_connection, table_name):
    df.to_sql(table_name,sql_connection, if_exists = "replace", index = False)

def run_query(query_statement, sql_connection):
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)

def log_process(message):
    time_format = "%d-%h-%Y %H:%M:%S"
    now = datetime.now().strftime(time_format)
    with open("./etl_project_log.txt","a") as f:
        f.write(now + " : " + message + "\n")

log_process("ETL process start")

df = extract(url, table_attribs)

log_process("Extract data complete")

df = transform(df)

log_process("Transform data complete")

load_to_csv(df, csv_path)

log_process("Load data to file CSV complete")

sql_connection = sqlite3.connect(db_name)

load_to_db(df,sql_connection, table_name)

log_process("Load data to database complete")

query_statement = f"SELECT * FROM {table_name} WHERE GDP_USD_billions >= 100"
run_query(query_statement,sql_connection)

log_process("Select data complete")

log_process("Process complete")

sql_connection.close()



    
