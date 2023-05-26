from user import *


class customer(CreateUser):
    def __init__(self, name, age, usern, pw):
        super().__init__(name, age, usern, pw)
        self.ticketBought = []
        self.debitCard = []
        self.creditCard = []

    def addTicket(self, ticket):
        self.ticketBought.append(ticket)

    def getTicket(self):
        return self.ticketBought

    def addCreditCard(self, credit):
        self.creditCard.append(credit)

    def addDebitCard(self, debit):
        self.debitCard.append(debit)
