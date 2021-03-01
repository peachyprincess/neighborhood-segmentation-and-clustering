import requests
from bs4 import BeautifulSoup

data = requests.get('https://en.wikipedia.org/wiki/Category:Neighbourhoods_in_Toronto').text
soup = BeautifulSoup(data, 'html.parser')
# print(soup.prettify())

for category_group in soup.find_all('div', class_='mw-category-group'):
    print('--- A New Category ---')
    for row in category_group.findAll("li"):
        print(row.text)
