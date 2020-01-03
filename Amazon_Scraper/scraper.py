import requests
from bs4 import BeautifulSoup
from smptlib import SMTP

# This is the URL we used to check the price of the product
URL = "https://www.amazon.in/GoPro-Black-Shorty-Rechargeable-Battery/dp/B07XP45RW1/ref=sr_1_5?keywords=gopro&qid=1578118748&sr=8-5"


    #
def check_price():
    headers = {
        "User-agent": "Mozilla/5.0 (Macintosh;  Intel Mac OS X 10.15; rv:71.0) Gecko/    20100101 Firefox/71.0"
    }

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content,  "html.parser")


    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    price = price.replace(",", "")
    converted_price = float(price[1:])
    if (converted_price < 25000):
        sendmail()



def sendmail():
    server = SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('[email-address]', '[generated-password]')
    subject = 'Price Fell Down'
    body = 'Check the amazon link https://www.amazon.in/GoPro-Black-Shorty-Rechargeable-Battery/dp/B07XP45RW1/ref=sr_1_5?keywords=gopro&qid=1578118748&sr=8-5'

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        [from],
        [to],
        msg
    )
    print('Email has been sent')



check_price()
