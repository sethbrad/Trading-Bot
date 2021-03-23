import cbpro
import json

with open("./secret.json") as json_file:
    secret = json.load(json_file)

authClient = cbpro.AuthenticatedClient(secret["apiKey"], secret["apiSecret"], secret["passphrase"],
                                       api_url="https://api.pro.coinbase.com")

with open("accIDs.json") as json_file:
    accIDs = json.load(json_file)


# API functions
def getAcc(acc):  # id set to XRP account
    return authClient.get_account(accIDs[acc])


def getPrice(acc):
    return 0


def buy(funds):
    authClient.place_market_order(product_id="XRP-USD", side="buy", funds=funds)


def sell(funds):
    return 0


def getOrders():
    orderList = authClient.get_orders()
    print(list(orderList))
