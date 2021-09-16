# For the purpose of testing small amount of code

# Imports
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Stating which site will be scraped
site = "https://tracker.habhub.org/#!mt=roadmap&mz=12&qm=1_day&f=PC4L-R" # https://spacenear.us/tracker/datanew.php?mode=1day&type=positions&format=json&vehicles=St_Oscar"

# Installing and opening the web driver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Finding the site to be scraped
driver.get(site)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

print(soup)

# print(soup.select('position'))
# returns JSON object as
# a dictionary
# data = json.load(soup)
#
# # Iterating through the json
# # list
# for i in data['position']:
#     print(i)

