import api
import DummyAPI
import time

import pandas as pd

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

""" class buySell():

    buySet = False
    sellSet = False

    def __init__(self):
        pass

    def setBuy(self, buyPrice):
        self.buyPrice = buyPrice

    def setSell(self, sellPrice):
        self.sellPrice = sellPrice

    def getProfit(self):
        if (self.buySet and self.sellSet):
            self.buySet = False
            self.sellSet = False
            return self.sellPrice - self.buyPrice
        else:
            return "buySell not completed!"

    def getData(self): """

##########

lastPrice = 0.0
profit = 0.0
transactions = []
prices = []


def main():
    global lastPrice
    lastPrice = float(input("Enter last price for the crypto: "))

    try:
        while (1):
            trade()
            print("Profit: ", profit)
            time.sleep(5)
    except KeyboardInterrupt:
        dataOut()
        return


##########

def trade():
    global state, profit

    if state == 0:  # buying
        if attemptBuy():
            profit -= DummyAPI.getDPrice()
        else:
            return

    else:  # selling
        if attemptSell():
            profit += DummyAPI.getDPrice()
        else:
            return


def attemptBuy():
    global lastPrice, state, transactions, prices
    price = DummyAPI.getDPrice()

    percentDiff = (price - lastPrice) / lastPrice * 100.0

    if (percentDiff > DIP_TH or percentDiff > UPWARD_TH) and DummyAPI.getMoney() > (price / 10):
        DummyAPI.dBuy(price / 10)
        transactions.append("buy")
        prices.append(price)

        state = not state
        # log("Buy completed.\n")

        lastPrice = price
        return True

    lastPrice = price
    return False


def attemptSell():
    global lastPrice, state, transactions, prices
    price = DummyAPI.getDPrice()

    percentDiff = (price - lastPrice) / lastPrice * 100.0

    if (percentDiff > PROFIT_TH or percentDiff < DOWNWARD_TH) and DummyAPI.getStock() > (price / 10):
        DummyAPI.dSell(price / 10)
        transactions.append("sell")
        prices.append(price)

        state = not state
        # log("Sell completed.\n")

        lastPrice = price
        return True

    lastPrice = price
    return False


def log(msg):  # expand with more details
    logFile = open("log.txt", "a")

    logFile.write(msg)
    logFile.write(time.asctime())
    logFile.write("\n")

    logFile.close()


def dataOut():
    my_df = {"Action": transactions,
             "Price": prices}

    df = pd.DataFrame(my_df)
    data = df.to_csv("data.csv", index=True)


# # # # #
main()
dataOut()
# # # # #
