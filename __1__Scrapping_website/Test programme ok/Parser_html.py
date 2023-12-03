import requests
from bs4 import BeautifulSoup

url = "https://www.cuisinez-pour-bebe.fr/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
#Si on veux trouver le titre, on cherche dans soup qui contient la page
print(type(soup))
