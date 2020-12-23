import requests
from urllib.request import urlopen
import re


def run(api_key, flag, choice):
    if choice.upper() == "RT":
        while flag:
            print("[Real Time Stock Price]")
            ticker = input("Please enter ticker: ")
            url = "https://financialmodelingprep.com/api/v3/quote-short/{}?apikey={}".\
                format(ticker, api_key)
            data = requests.get(url).json()
            print(parse(data))
            decision = input("Another quote? Y/N: ")
            if decision.upper() == "N":
                flag = False
            print()
    elif choice.upper() == 'HP':
        while flag:
            print("[Historical Stock Price]")
            ticker = input("Please enter ticker: ")
            start_date = input("Enter start date (format: yyyy-mm-dd): ")
            end_date = input("Enter end date (format: yyyy-mm-dd): ")
            url = urlopen("https://financialmodelingprep.com/api/v3/historical-price-full/{}?from={}&to={}&apikey={}".
                        format(ticker, start_date, end_date, api_key))
            print(re.sub('[{},"]', "", url.read().decode("utf-8")))

            decision = input("Another quote? Y/N: ")
            if decision.upper() == "N":
                flag = False
            print()


def parse(data):
    parsed = "Symbol: {}\n".format(data[0]['symbol']) + \
             "Price: ${}\n".format(data[0]['price']) + \
             "Volume: {:,}".format(data[0]['volume'])
    return parsed


def main():
    api_key = input("Enter API key: ")
    choice = input("Enter 'RT' for real time price or 'HP' for historical price: ")
    print()
    flag = True
    run(api_key, flag, choice)


if __name__ == "__main__":
    main()
