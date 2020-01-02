import requests
from bs4 import BeautifulSoup

# This is the URL we used to check the price of the product
URL = "https://www.amazon.in/GoPro-Black-Shorty-Rechargeable-Battery/dp/B07XP45RW1/ref=sr_1_5?keywords=gopro&qid=1578118748&sr=8-5"

#
headers = {
    "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:71.0) Gecko/20100101 Firefox/71.0"
}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")


title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
price = price.replace(",", "")
converted_price = float(price[1:])
print(title.strip())
print(price)
print(converted_price)
