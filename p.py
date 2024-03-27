from bs4 import BeautifulSoup
import requests
import pandas as pd
products = []
url = "https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
div = soup.select("div._4rR01T")
for divs in div:
    products.append(divs.string)
df = pd.DataFrame({'':products})
df.to_csv("product1.csv",index=False,encoding="utf-8")

