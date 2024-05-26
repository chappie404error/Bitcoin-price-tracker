import requests
import smtplib
from datetime import datetime

MY_EMAIL = "chap#####hu@gmail.com"
MY_PASSWORD = "xb#########tzq"


def get_bitcoin_price_from_coindesk():
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    response = requests.get(url)
    data = response.json()
    price = data["bpi"]["USD"]["rate"]
    return round(float(price.replace(',', '')))


def get_bitcoin_price_from_coingecko():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    price = data["bitcoin"]["usd"]
    return price


def get_bitcoin_price_from_binance():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url)
    data = response.json()
    price = data["price"]
    return round(float(price))


final_verdict = (f" BIT COIN PRICE \n"
                 f"COINDESK = {get_bitcoin_price_from_coindesk()}\n"
                 f"COINGECKO = {get_bitcoin_price_from_coingecko()}\n"
                 f"BINANCE = {get_bitcoin_price_from_binance()} \n"

                 )

time_now = datetime.now()

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(MY_EMAIL, MY_PASSWORD)
connection.sendmail(
    from_addr=MY_EMAIL,
    to_addrs="prath######gmail.com",
    msg=f"subject: BTC price comparison \n\nBTC price:\nTIME= {time_now}\n{final_verdict}"
)
print("EMAIL SENT SUCCESSFULLY")
connection.close()
