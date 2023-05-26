from abc import ABC, abstractmethod
import random

class Card():
    
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.number = ""
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)    
        
    def setBalance(self, balance):
        pass
        
    def setPin(self, pin):
        pass
        
    def setNumber(self):
        num = ""
        if len(self.number) == 0:
            for i in range(8):
                num += str(random.randint(1, 9))
            return num
        
    def charge(self, amount):
        pass

    def setCard(self):
        num = ""
        if len(self.number) == 0:
            for i in range(8):
                num += str(random.randint(1, 9))
            return num


if __name__ == '__main__':
    obj1 = Card("ja", 26)
    print(obj1)
    
    