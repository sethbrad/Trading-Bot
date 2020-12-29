import time, api, dummyAPI

# Bot has BUYING and SELLING state
# Access transactions and data through Coinbase

# 0 if buying, 1 if selling
state = 0 

# buy thresholds
DIP_TH = 0.05
UPWARD_TH = -0.05

# sell thresholds
PROFIT_TH = 0.05
DOWNWARD_TH = -0.05

##########

lastPrice = 0.0 # hard code this?

def main():
    global lastPrice
    lastPrice = float(input("Enter last price for the crypto: "))

    while(1):
        trade()
        time.sleep(10)

##########

def trade():
    global state

    if(state == 0): # buying
        attemptBuy()
        
    else: # selling
        attemptSell()

def attemptBuy():
    global lastPrice, state
    price = dummyAPI.getDPrice()

    percentDiff = (price - lastPrice) / lastPrice * 100.0

    if((percentDiff > DIP_TH or percentDiff > UPWARD_TH) and dummyAPI.getMoney() > (price/20)):
        dummyAPI.dBuy(price / 20)
        state = not state
        log("Buy completed.\n")

    lastPrice = price

def attemptSell():
    global lastPrice, state
    price = dummyAPI.getDPrice()

    percentDiff = (price - lastPrice) / lastPrice * 100.0

    if((percentDiff > PROFIT_TH or percentDiff < DOWNWARD_TH) and dummyAPI.getStock() > (price/20)):
        dummyAPI.dSell(price / 20)
        state = not state
        log("Sell completed.\n")

    lastPrice = price

def log(msg): # expand with more details
    logFile = open("log.txt", "a")

    logFile.write(msg + "\n")
    logFile.write(time.asctime())

    logFile.close()

# # # # #
main()
# # # # #