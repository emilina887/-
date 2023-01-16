import requests
from bs4 import BeautifulSoup
import lxml
import fake_useragent

url = f'https://allo.ua/ua/roboty-pylesosy/'
headers = {"user-agent": fake_useragent.UserAgent().random}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
products = soup.find("div", class_="products-layout__container products-layout--grid")
product_all = products.find_all("div", class_="product-card")
for product in product_all:
    title = product.find("a", class_="product-card__title")
    price = product.find("div", class_="v-pb")
    print(price.text)
    print(title.text)
    with open('products.txt', 'a', encoding='utf-8') as file:
        file.write(f'{title.text}\n')
        file.write(f'{price.text}\n')
