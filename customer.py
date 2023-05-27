from user import *


class Customer(CreateUser):
    def __init__(self, name, age, usern, pw):
        super().__init__(name, age, usern, pw)
        self.ticketBought = []
        # self.debitCard = []
        # self.creditCard = []
        self.cards = []

    def addTicket(self, ticket):
        self.ticketBought.append(ticket)

    def getTicket(self):
        return self.ticketBought

    # def addCreditCard(self, credit):
    #     self.creditCard.append(credit)
    #
    # def addDebitCard(self, debit):
    #     self.debitCard.append(debit)

    def addCards(self, card):
        self.cards.append(card)

    # def getCreditCard(self, i):
    #     return self.creditCard[i]
    #
    # def getDebitCard(self, i):
    #     return self.debitCard[i]

    def getCards(self):
        return self.cards

    def cardsToString(self):
        for cards in self.cards:
            print(cards)

    def __str__(self):
        info = "Username: " + self.usern + "\n"
        info += "Name: " + self.name + "\n"
        info += "Age: " + str(self.age) + "\n"
        info += "Password: " + str(self.pw) + "\n"
        info += "Tickets Bought: " + str(self.ticketBought) + "\n"
        info += "Cards: " + str(self.cards) + "\n"
        return info
