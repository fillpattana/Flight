from card import Card
from user import CreateUser
import random

class DebitCard(Card, CreateUser):
    
    def __init__(self, name, age, usern, pw, pin):
        super().__init__(name, age, usern, pw, pin)
        self.pin = pin
        self.balance = 0
        self.number = ""
        
    def getName(self):
        return self.name    
        
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
        info += "Username: " + self.usern + "\n"
        info += "Password: " + str(self.pw) + "\n"
        info += "Pin: " + str(self.pin) + "\n"
        info += "Balance: " + str(self.balance) + "\n"
        info += "Number: XXXX" + self.number[4:] + "\n"
        return info
    
    
    
    

if __name__ == '__main__':
    card1 = DebitCard("ja", 22, "k", "i", 11)
    print(card1)
    
