import time, api

# Bot has BUYING and SELLING state
# Access transactions and data through Coinbase

logFile = open("log.txt", "a")

# 0 if buying, 1 if selling
state = 0 

# buy thresholds
DIP_TH = 0.05
UPWARD_TH = -0.05

# sell thresholds
PROFIT_TH = 0.05
DOWNWARD_TH = -0.05

##########

def main():
    while(1):
        trade()
        time.sleep(60)
    logFile.close()

##########

lastPrice = 100.0 # hard code this?

def trade():
    if(state == 0): # buying
        attemptBuy()
        
    else: # selling
        attemptSell()

def attemptBuy():
    percentDiff = (api.getPrices() - lastPrice) / lastPrice * 100.0
    if(percentDiff > DIP_TH or percentDiff > UPWARD_TH):
        api.buy()
        state = not state
        log("Buy completed.\n")

def attemptSell():
    percentDiff = (api.getPrices() - lastPrice) / lastPrice * 100.0
    if(percentDiff > PROFIT_TH or percentDiff < DOWNWARD_TH):
        api.sell()
        state = not state
        log("Sell completed.\n")

def log(msg):
    print(msg)
    print(time.asctime())

    logFile.write(msg)
    logFile.write(time.asctime())

# api.buy(1.00)