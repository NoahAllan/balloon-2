# For the purpose of testing small amount of code

# Imports
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json
import urllib
import requests

url = "https://legacy-snus.habhub.org/tracker/datanew.php?mode=1day&type=positions&format=json&max_positions=0&" \
      "position_id=86480312&vehicles=St_Oscar"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
print(data)
data2 = data['positions']
data3 = data2['position']
data4 = data3[0]
data5 = data4['data']
if data4["vehicle"] == 'St_Oscar':
    print('Found')
else:
    print('fail')
