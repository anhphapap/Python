import pandas as pd 
import glob 
import xml.etree.ElementTree as ET
from datetime import datetime

log_file = 'log.txt'
transformed_data = "transformed_data.csv"

def extract_from_csv(file):
    data = pd.read_csv(file)
    return data

def extract_from_json(file):
    data = pd.read_json(file, lines=True)
    return data

def extract_from_xml(file):
    data = pd.DataFrame(columns=["car_model","year_of_manufacture","price","fuel"])
    tree = ET.parse(file)
    root = tree.getroot()
    for element in root:
        e1 = element.find("car_model").text
        e2 = int(element.find("year_of_manufacture").text)
        e3 = float(element.find("price").text)
        e4 = element.find("fuel").text
        data = pd.concat([data, pd.DataFrame([{"car_model":e1, "year_of_manufacture":e2, "price":e3, "fuel":e4}])],ignore_index=True)
    return data
print(type(extract_from_xml("used_car_prices2.xml")))

def extract():
    data = pd.DataFrame(columns=["car_model","year_of_manufacture","price","fuel"])
    for x in glob.glob("*.csv"):
        data = pd.concat([data, extract_from_csv(x)],ignore_index=True)
    for x in glob.glob("*.json"):
        data = pd.concat([data, extract_from_json(x)], ignore_index=True)
    for x in glob.glob("*.xml"):
        data = pd.concat([data, extract_from_xml(x)], ignore_index=True)
    return data

def transform(data):
    data['price'] = round(data['price'],2)

def load(data):
    data.to_csv(transformed_data)

def log(message):
    time_format = "%D-%h-%Y %H:%M:%S"
    now = datetime.now().strftime(time_format)
    with open(log_file, 'a') as f:
        f.write(now+", "+message+"\n")

#Main

log("ETL Job Started")

log("Extract Data Started")

extracted_data = extract()

log("Extract Data Ended")

log("Transform Data Started")

transform(extracted_data)

log("Transform Data Ended")

log("Load Data Started")

load(extracted_data)

log("Load Data Ended")

log("ETL Job Ended")

print(extract_from_csv("transformed_data.csv"))
