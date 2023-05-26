from card import Card


class DebitCard(Card):
    
    def __init__(self, name, pin, balance):
        super().__init__(name, pin)
        self.balance = balance
        self.number = self.setNumber()
        
    def getName(self):
        return self.name    
        
    def getPin(self):
        return self.pin
    
    def getBalance(self):
        return self.balance
    
    def getNumber(self):
        return self.number
    
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
        info += "Pin: " + str(self.pin) + "\n"
        info += "Balance: " + str(self.balance) + "\n"
        info += "Number: XXXXX" + self.number[5:] + "\n"
        return info
    
    
    
    

if __name__ == '__main__':
    card1 = DebitCard("jackson ho", 1234, 1000)
    print(card1)
    
