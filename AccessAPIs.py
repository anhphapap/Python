import requests
from bs4 import BeautifulSoup

# Specify the URL of the webpage you want to scrape
url = 'https://en.wikipedia.org/wiki/IBM'

# Send an HTTP GET request to the webpage
response = requests.get(url)

# status_code == 200 => OK
print(response.status_code == 200)

# Store the HTML content in a variable
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Display a snippet of the HTML content
# print(html_content[:500])

# Find all <a> tags in the HTML
tag_a = soup.find_all('a')

# print(tag_a[0])

import os

url_img = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'

r = requests.get(url_img)

# Get path of Image 
path = os.path.join(os.getcwd(),"image.png")

# Save image
with open(path,"wb") as f:
    f.write(r.content)

# url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt"
# Download the txt file in the given link
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt"
path = os.path.join(os.getcwd(),"example1.txt")
rt = requests.get(url)
with open(path, "wb") as f:
    f.write(rt.content)

# Random User API
from randomuser import RandomUser 
import pandas as pd

r = RandomUser()
list =  r.generate_users(10)
# Get Fullname and email from list user
for user in list:
    print(user.get_full_name()," ",user.get_email())

# Fruityvice API
import json as js
url_fruit = "https://fruityvice.com/api/fruit/all"
data_fruit = requests.get(url_fruit)
data_fruit = js.loads(data_fruit.text)
df_fruit = pd.DataFrame(data_fruit)
print(df_fruit)
# Fix the column contain multiple subcolumns  
df_fruit = pd.json_normalize(data_fruit)
print(df_fruit)

# Official Joke API
url_joke = "https://official-joke-api.appspot.com/jokes/ten"
data_joke = js.loads(requests.get(url_joke).text)
res = pd.DataFrame(data_joke)
print(res)