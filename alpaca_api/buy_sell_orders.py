import alpaca_trade_api as tradeapi
import time

key = "AKXSOWSZ8KAC4I4GSSDD"
sec = "c3p2zDOsSFuKQcPLRbXwbKa2K5ntkCqdO58U2qoQ"

url = "https://paper-api.alpaca.markets"

api = tradeapi.REST(key, sec, url, api_version='v2')
account = api.get_account()

print(account.status)
inpt = input("Enter 1(buy) or 2(sell)")

if inpt == 1:
    order = api.submit_order(
    id: "64bbff51-59d6-4b3c-9351-13ad85e3c752",
    "class": "crypto",
    "exchange": "FTXU",
    "symbol": "BTCUSD",
    "name": "Bitcoin",
    "status": "active",
    "tradable": true,
    "marginable": false,
    "shortable": false,
    "easy_to_borrow": false,
    "fractionable": true)
    time.sleep(5)
    print(order)

elif inpt == 2:
    order = api.submit_order("id": "64bbff51-59d6-4b3c-9351-13ad85e3c752",
    "class": "crypto",
    "exchange": "FTXU",
    "symbol": "BTCUSD",
    "name": "Bitcoin",
    "status": "active",
    "tradable": true,
    "marginable": false,
    "shortable": false,
    "easy_to_borrow": false,
    "fractionable": true)
    time.sleep(5)
    print(order)

else:
    print("Invalid input")

