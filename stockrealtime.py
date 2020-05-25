import bs4
import requests
from bs4 import BeautifulSoup

def parsePrice():
    url = requests.get("https://finance.yahoo.com/quote/aapl/news?ltr=1")
    soup = bs4.BeautifulSoup(url.text, features="html.parser")
    price = soup.find_all("div", {"class": 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price

while True:
    print("The current price of Apple: " + str(parsePrice()))



