import cbpro, json

with open("secret.json") as json_file:
    secret = json.load(json_file)

authClient = cbpro.AuthenticatedClient(secret["apiKey"], secret["apiSecret"], secret["passphrase"], api_url="https://api.pro.coinbase.com")

with open("xrp.json") as json_file:
    xrp = json.load(json_file)

# API functions
def getAcc(): # id set to XRP account 
    return authClient.get_account(xrp["id"])

def getPrices():
    return 0

def buy(funds):
    authClient.place_market_order(product_id="XRP", side="buy", funds=funds)
    orderList = authClient.get_orders()
    print(list(orderList))

def sell():
    return 0