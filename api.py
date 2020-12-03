import cbpro, json, base64

with open("secret.json") as json_file:
    secret = json.load(json_file)

authClient = cbpro.AuthenticatedClient(secret["apiKey"], secret["apiSecret"], secret["passphrase"], api_url="https://api.pro.coinbase.com")

# API functions
def getBalances():
    return 0

def getPrices():
    return 0

def buy():
    return 0

def sell():
    return 0