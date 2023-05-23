from Payment import card

class creditCard(card):
    def __init__(self, name, balance, pin):
        self.name = name
        self.balance = balance
        self.pin = pin
        
    def getBalance(self):
        return self.balance