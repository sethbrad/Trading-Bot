import random


class DummyAPI:

    def __init__(self, money, stock, price):
        self.money = money
        self.stock = stock
        self.price = price

    def getMoney(self):
        return self.money

    def getStock(self):
        return self.stock

    # gets a new market price with fluctuations
    def getDummyPrice(self):
        start = round(self.price - (self.price / 20))
        stop = round(self.price + (self.price / 20))

        price = random.randrange(start, stop, 1)
        return price

    def buy(self, funds):
        if self.money - funds < 0:
            print("Error: not enough money!")
            return

        self.stock += funds
        self.money -= funds
        print("Money: " + str(self.money) + " " + "Crypto: " + str(self.stock) + " " + "Price: " + str(self.price))

    def sell(self, funds):
        if self.stock - funds < 0:
            print("Error: not enough stock!")
            return

        self.money += funds
        self.stock -= funds
        print("Money: " + str(self.money) + " " + "Crypto: " + str(self.stock) + " " + "Price: " + str(self.price))


# # # # #

""" 
    while(1):
        print(getMoney())
        print(getStock())

        cmd = input()
    
        if(cmd == "deposit"):
            deposit(float(input("Enter amount: ")))
    
        if(cmd == "buy"):
            amount = float(input("Enter amount: "))
            dBuy(amount)
    
        if(cmd == "sell"):
            amount = float(input("Enter amount: "))
            dSell(amount)
    
        if(cmd == "done"):
            break 
"""
