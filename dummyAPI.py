import random

stock = 0.0
money = 1000.0
price = 100.0

def getMoney():
    global money
    return money

def getStock():
    global stock
    return stock

def deposit(amount):
    global money
    money += amount

def getDPrice():
    global price

    start = round(price - (price / 20))
    stop = round(price + (price / 20))

    price = random.randrange(start, stop, 1)
    return price

def dBuy(funds):
    global stock, money
    if (money - funds < 0):
        print("Error: not enough money!")
        return

    stock += funds
    money -= funds
    print("Money: " + str(money) + " " + "Crypto: " + str(stock) + " " + "Price: " + str(price))

def dSell(funds):
    global stock, money
    if (stock - funds < 0):
        print("Error: not enough stock!")
        return
        
    money += funds
    stock -= funds
    print("Money: " + str(money) + " " + "Crypto: " + str(stock) + " " + "Price: " + str(price))

# # # # #

""" while(1):
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
        break """