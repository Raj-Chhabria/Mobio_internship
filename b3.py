import requests
from bs4 import BeautifulSoup
import pandas as pd

with open('test.html') as html_file:
    soup = BeautifulSoup(html_file,'lxml')

table = soup.find('table',class_="test")
df = pd.read_html(str(table))

print(df)