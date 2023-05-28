from card import Card


class CreditCard(Card):

    def __init__(self, name, pin):
        super().__init__(name, pin)
        self.credit = 0
        self.limit = 100000
        self.number = self.setNumber()

    def getName(self):
        return self.name

    def getPin(self):
        return self.pin

    def getCredit(self):
        return self.credit

    def getBalance(self):
        return self.limit

    def setLimit(self, limit):
        self.limit = limit

    def getNumber(self):
        return self.number

    # charging credit card
    def charge(self, amount):
        if amount > self.limit or amount < 0:
            print("charge denied\n")
        else:
            self.credit += amount
            self.limit -= amount
            print("remaining limit: " + str(self.limit) + "\n")

    # paying for credit card
    def payCredit(self, amount):
        if self.credit == 0 or amount <= 0:
            print("Payment Denied\n")
        else:
            self.credit -= amount
            self.limit += amount

    def __str__(self):
        info = "Name: " + self.name + "\n"
        info += "Pin: " + str(self.pin) + "\n"
        info += "Credit: " + str(self.credit) + "\n"
        info += "Limit: " + str(self.limit) + "\n"
        info += "Number: XXXXX" + self.number[5:] + "\n"
        return info
