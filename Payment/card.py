from abc import ABC, abstractmethod

class Card(ABC):
    
    def __init__(self, name, balance, pin):
        self.name = name
        self.balance = balance
        self.pin = pin
        self.number = ""
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)
        
    @abstractmethod
    def charge(self, amount):
        pass







if __name__ == '__main__':
    obj1 = Card("ja", "jo", 1, 000, 2)
    print(obj1.name)