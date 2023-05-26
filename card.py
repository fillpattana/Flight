from abc import ABC, abstractmethod
import sys
# sys.path.append('/Users/akararatpattanamontri/Documents/FlightSEP/Flight/User')
# # from Ticket.flightTicket import*
# from User.user import *

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
        
    def setNumber(self, number):
        pass
        
    def charge(self, amount):
        pass


if __name__ == '__main__':
    obj1 = Card("ja", 26, "k", "k", 500, 1111)
    print(obj1)
    
    