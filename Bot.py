import api
import DummyAPI
import time

import pandas as pd

# Bot has BUYING and SELLING state
# Access transactions and data through Coinbase

# buy thresholds
DIP_TH = 0.05
UPWARD_TH = -0.05

# sell thresholds
PROFIT_TH = 0.05
DOWNWARD_TH = -0.05


def log(msg):  # expand with more details
    logFile = open("log.txt", "a")

    logFile.write(msg)
    logFile.write(time.asctime())
    logFile.write("\n")

    logFile.close()


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


class Bot:

    def __init__(self):
        # 0 if buying, 1 if selling
        self.state = 0
        self.lastPrice = float(input("Enter last price traded at: "))
        self.profit = 0

        self.transactions = []
        self.prices = []

        self.dummy = DummyAPI.DummyAPI(1000, 0, 100)

    def main(self):

        try:
            while 1:
                self.trade()
                print("Profit: ", self.profit)
                time.sleep(5)
        except KeyboardInterrupt:
            self.dataOut()
            return

    def trade(self):
        if self.state == 0:  # buying
            if self.attemptBuy():
                self.profit -= self.dummy.getDummyPrice()
            else:
                return

        else:  # selling
            if self.attemptSell():
                self.profit += self.dummy.getDummyPrice()
            else:
                return

    def attemptBuy(self):
        price = self.dummy.getDummyPrice()

        percentDiff = (price - self.lastPrice) / self.lastPrice * 100.0

        if (percentDiff > DIP_TH or percentDiff > UPWARD_TH) and self.dummy.getMoney() > (price / 10):
            self.dummy.buy(price / 10)
            self.transactions.append("buy")
            self.prices.append(price)

            self.state = not self.state
            # log("Buy completed.\n")

            self.lastPrice = price
            return True

        self.lastPrice = price
        return False

    def attemptSell(self):
        price = self.dummy.getDummyPrice()

        percentDiff = (price - self.lastPrice) / self.lastPrice * 100.0

        if (percentDiff > PROFIT_TH or percentDiff < DOWNWARD_TH) and self.dummy.getStock() > (price / 10):
            self.dummy.sell(price / 10)
            self.transactions.append("sell")
            self.prices.append(price)

            self.state = not self.state
            # log("Sell completed.\n")

            self.lastPrice = price
            return True

        self.lastPrice = price
        return False

    def dataOut(self):
        my_df = {"Action": self.transactions,
                 "Price": self.prices}

        df = pd.DataFrame(my_df)
        df.to_csv("data.csv", index=True)


# # # # #
bot = Bot()

bot.main()
bot.dataOut()
# # # # #
