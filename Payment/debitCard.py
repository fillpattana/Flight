from card import Card
import random

class debitCard(Card):
    
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.balance = 0
        self.number = ""
        
    def getPin(self):
        return self.pin
    
    def getBalance(self):
        return self.balance
    
    def getNumber(self):
        return self.number
    
    #generate random 6 digit debit card number
    def setNumber(self):
        num = ""
        if len(self.number) == 0:
            for i in range(6):
                num += str(random.randint(1, 9))
            self.number = num
        else:
            print("debit card number already exists.\n")
    
    #charging debit card
    def charge(self, amount):
        if amount > self.balance or amount < 0:
            print("charge denied\n")
        else:
            self.balance -= amount
    
    #top up
    def topUp(self, amount):
        if amount < 0:
            print("Invalid Amount\n")
        else:
            self.balance += amount
    
    def __str__(self):
        info = "Name: " + self.name + "\n"
        info += "Pin: " + self.pin + "\n"
        info += "Balance: " + str(self.balance) + "\n"
        info += "Number: XXXX" + self.number[4:] + "\n"
        return info
    
    
    
    

if __name__ == '__main__':
    card1 = debitCard("Jackson Blue", "1111")
    # card1.setNumber()
    # print(card1)
    # card1.setNumber()
    # print(card1)
    # card1.topUp(1000)
    # print(card1)
    # card1.charge(1000)
    print(card1)
    
