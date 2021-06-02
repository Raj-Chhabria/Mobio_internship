from bs4 import BeautifulSoup
import requests

with open('test.html') as html_file:
    soup = BeautifulSoup(html_file,'lxml')

#print(soup.prettify()) to get entire html code of the webpage

# for printing only the text of title
#match = soup.title.text

# To get text of div tag who has class = footer

# match = soup.find('div',class_="footer").text

# To print text from a particular tag of div tag 

# Here paragraph tag is wriiten inside the div tag with class = testclass

# and we have to print text written between the p tags

# for finding all such tags we can use find_all instead of find

# div_testclass = soup.find('div',class_="testclass")

# para = div_testclass.p.text

# print(para)

