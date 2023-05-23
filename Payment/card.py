from abc import ABC, abstractmethod

class Card(ABC):
    def __init__(self, name, balance, pin):
            self.name = name
            self.balance = balance
            self.pin = pin
            
    @abstractmethod
    def getBalance(self):
        return self.balance
    
    def setBalance(self, b):
        self.balance += b
        
    def addCard(self):
        pass
        
    