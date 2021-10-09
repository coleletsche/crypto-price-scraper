import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
from termcolor import colored

UP = "\u25B2"
DOWN = "\u25BC"
NONE = "\u25A0"
 
QUERY_BUFFER_TIME = 30
REQUEST_BUFFER = 0

COIN_URLS = {
        "BTC" : "https://coinmarketcap.com/currencies/bitcoin/",
        "ETH" : "https://coinmarketcap.com/currencies/ethereum/",
        "XRP" : "https://coinmarketcap.com/currencies/ripple/",
        "LTC" : "https://coinmarketcap.com/currencies/litecoin/",
        "DOT" : "https://coinmarketcap.com/currencies/polkadot/",
        "ADA" : "https://coinmarketcap.com/currencies/cardano/",
        "DOGE" : "https://coinmarketcap.com/currencies/dogecoin/",
        "DASH" : "https://coinmarketcap.com/currencies/dash/"
        }

prev_prices = {
        "BTC" : 1,
        "ETH" : 1,
        "XRP" : 1,
        "LTC" : 1,
        "DOT" : 1,
        "ADA" : 1,
        "DOGE" : 1,
        "DASH" : 1 
        }

print(colored(UP + " increase", "green"))
print(colored(DOWN + " decrease", "red"))
print(colored(NONE + " none", "white"))

iterations = 0

while True:

    print("====================================================")
    print("|     SCRAPING COINMARKETCAP FOR CRYPTO PRICES     |")
    print("====================================================")

    for key in COIN_URLS:
        try:
            page = requests.get(COIN_URLS[key])
            soup = BeautifulSoup(page.content, 'html.parser')
            price = float(soup.find('div', class_='priceValue').text[1:].replace(',', ''))
        except AttributeError:
            continue

        precent_change = ((price - prev_prices[key]) / prev_prices[key]) * 100

        if precent_change == 0 or iterations == 0:
            print('| The price of %s is currently: $%.3f USD\t   | %s' %(key, price, colored(NONE + " 0%", "white")))
        elif precent_change > 0:
            print('| The price of %s is currently: $%.3f USD\t   | %s' %(key, price,
                colored(UP + " %.2f%%" %(precent_change), "green")))
        else:
            print('| The price of %s is currently: $%.3f USD\t   | %s' %(key, price, 
                colored(DOWN + " %.2f%%" %(precent_change), "red")))

        prev_prices[key] = price

        with open("price_history.txt", "a") as f:
            f.write("%s %s %s\n" %(key, str(price), datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

        time.sleep(REQUEST_BUFFER)
        
    print("====================================================")
    print("\nSleeping...\n")

    iterations += 1

    time.sleep(QUERY_BUFFER_TIME)
