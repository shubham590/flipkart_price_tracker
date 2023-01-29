import requests
from bs4 import BeautifulSoup
import telepot
import time


def send_message(chat_id, message):
    bot = telepot.Bot('6001631018:AAEOtxu73yJfJTUbtGjK8dpgNyuSchEdHjo')
    bot.sendMessage(chat_id, message)



def fun():
    url = "https://www.flipkart.com/tp-link-archer-c6-mu-mimo-gigabit-1200-mbps-wireless-router/p/itmc4672304ef179?pid=RTRGYSZRVXDXQGRS&lid=LSTRTRGYSZRVXDXQGRSPULPKE&marketplace=FLIPKART&q=archer+6&store=6bo&spotlightTagId=BestsellerId_6bo&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=5579a22a-1332-41b0-926e-fcf2ee065468.RTRGYSZRVXDXQGRS.SEARCH&ppt=sp&ppn=sp&ssid=yb0z7337m80000001674997110421&qH=106fce5765d92d00"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    price = soup.find("div", {"class": "_30jeq3 _16Jk6d"}).get_text()
    price = price.replace(",", "")
    price = int(price.replace("₹", ""))
    print(price)
    if price < 2799:
        send_message(1701014183, 'The price of the product has dropped!')


while True:
    fun()
    time.sleep(60)
