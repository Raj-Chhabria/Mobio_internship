import requests
from bs4 import BeautifulSoup
import pandas as pd

source = requests.get("https://www.amazon.in/s?k=mobiles+under+15%2C000&rh=n%3A976419031%2Cp_36%3A1318506031&dc&crid=1JQE0OMR5KBZ0&qid=1622091710&rnid=1318502031&sprefix=mobiles%2Caps%2C359&ref=sr_nr_p_36_4").text

soup = BeautifulSoup(source,'lxml')

match = soup.find('div',class_="s-matching-dir sg-col-16-of-20 sg-col sg-col-8-of-12 sg-col-12-of-16").text

print(match)
