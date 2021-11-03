from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Firefox()

ziel = [
    "https://www.wollplatz.de/wolle/dmc/dmc-natura-xl?sqr=dmc%20natura%20Xl&",
    "https://www.wollplatz.de/wolle/drops/drops-safran?sqr=drops%20safran&",
    "https://www.wollplatz.de/wolle/drops/drops-baby-merino-mix?sqr=drops%20baby%20merino%20mix&",
    "https://www.wollplatz.de/wolle/stylecraft/stylecraft-special-dk?sqr=stylecraft%20special&"
]

products = []
prices = []
nadelStarke = []
zusammenStellung = []

for p in ziel:
    driver.get(p)

    content = driver.page_source
    soup = BeautifulSoup(content)

    name = soup.find('h1', attrs={'id':'pageheadertitle'})

    price0 = soup.find('span', attrs={'class': 'product-price'})
    price = price0.find('span', attrs={'class':'product-price-amount'})

    ns0 = soup.find('td', text="Nadelstärke")
    ns = ns0.find_next_sibling()

    zu0 = soup.find('td', text="Zusammenstellung")
    zu = zu0.find_next_sibling()

    products.append(name.text)
    prices.append(price.text)
    nadelStarke.append(ns.text)
    zusammenStellung.append(zu.text)

df = pd.DataFrame({
    'Product Name': products,
    'Price': prices,
    'Nadelstärke': nadelStarke,
    'Zusammenstellung': zusammenStellung
})
df.to_csv('products.csv', index=False, encoding='utf-8')

driver.quit()
