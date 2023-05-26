from card import Card
# sys.path.append('/Users/akararatpattanamontri/Documents/FlightSEP/Flight/Ticket')

from ticketGenerator import *

class CreditCard(Card):

    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.credit = 0
        self.limit = 10000
        self.number = ""

    def getName(self):
        return self.name

    def getPin(self):
        return self.pin

    def getCredit(self):
        return self.credit

    def getLimit(self):
        return self.limit

    def getNumber(self):
        return self.number

    # generate random 8 digit credit card number
    def setNumber(self):
        num = ""
        if len(self.number) == 0:
            for i in range(8):
                num += str(random.randint(1, 9))
            self.number = num
        else:
            print("credit card number already exists.\n")

    # just in case limit's too low
    def setLimit(self, num):
        self.limit = num

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


if __name__ == '__main__':
    # card1 = CreditCard("Joe Son", 1111)
    # # flightTicket.getPrice()
    # # card1.setNumber()
    # # print(card1)
    # card1.charge(flightTicket.getPrice())
    # print(card1)

    # card1.charge(-1)
    # print(card1)
    # card1.payCredit(1000)
    # print(card1)

    name = "Kittiphong Thachaphat"
    desti = "Bangladesh"
    depart = "Japan"
    date = datetime.date(2023, 5, 27)
    a = getAvailableAirway("Japan", "Bangladesh")
    tickets = generateBusinessTicket(name, desti, depart, a, date)

    for t in tickets:
        print(t)
        print("\n")

    print("\n")
