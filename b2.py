from bs4 import BeautifulSoup
import requests

# to get source code of website
source = requests.get("http://coreyms.com").text


# printing source code using same procedure
soup = BeautifulSoup(source,'lxml')

# print(soup.prettify())

first_title = soup.find('h2',class_="entry-title").text

print(first_title)

for article in soup.find_all('article'):
    print(article.prettify())

    summary = soup.find('div',class_="entry-content")

    sfinal = summary.p.text

    print(sfinal)

    print()