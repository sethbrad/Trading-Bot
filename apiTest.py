import json, requests, time, base64, hmac, hashlib
from requests.auth import AuthBase

url = "https://api-public.sandbox.pro.coinbase.com"

with open("secret.json") as json_file:
    secret = json.load(json_file)

# custom header for API
class ExchangeAuth(AuthBase):
    def __init__(self, apiKey, apiSecret, passphrase):
        self.apiKey = apiKey
        self.apiSecret = apiSecret
        self.passphrase = passphrase

    def __call__(self, request):
        timestamp = str(time.time())
        message = timestamp + request.method + request.path_url + ""
        hmacKey = base64.b64decode(self.apiSecret)
        signature = hmac.new(hmacKey, message, hashlib.sha256) # something is wrong here
        sigB64 = signature.digest().encode("base64").rstrip("\n")

        request.headers.update({
            'CB-ACCESS-SIGN': sigB64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.apiKey,
            'CB-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        })
        return request

auth = ExchangeAuth(secret["apiKey"], secret["apiSecret"], secret["passphrase"])

# make request
r = requests.get(url + "accounts", auth=auth)
print(r.json())