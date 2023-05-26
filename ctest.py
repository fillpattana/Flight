import pickle

from creditCard import CreditCard
from debitCard import *
from customer import*
from ticketGenerator import *


def buyTicket(ticket, cust, i):
    if isinstance(cust.cards[i], CreditCard) and cust.cards[i].getLimit() > ticket.getPrice():
        price = cust.cards[i].getLimit() - ticket.getPrice()
        cust.cards[i].setLimit(price)
        cust.addTicket(ticket)
        for ticks in cust.getTicket():
            print("Ticket Bought")
            print(ticks)
        print("Card Limit: ", cust.cards[i].getLimit())
    elif isinstance(cust.cards[i], DebitCard) and cust.cards[i].getBalance() > ticket.getPrice():
        price = cust.cards[i].getBalance() - ticket.getPrice()
        cust.addTicket(ticket)
        cust.cards[i].setBalance(price)
        for ticks in cust.getTicket():
            print("Ticket Bought")
            print(ticks)
        print("Card Balance: ", cust.cards[i].getBalance())
    else:
        return "poor shit"

    # print(cust.cards[j].getBalance())

    # ticketprice = ticket.getPrice()
    # print("Chosen Ticket:", ticket.getPrice())
    # print("Customer Balance:", cust.creditCard[i].getLimit())


# name = "Kittiphong Thachaphat"
# desti = "Bangladesh"
# depart = "Japan"
# date = datetime.date(2023, 5, 27)
# a = getAvailableAirway("Japan", "Bangladesh")
# tickets = generateBusinessTicket(name, desti, depart, a, date)

customer1 = customer("Indiana Jay", 87, "jaja", "jeje")
card1 = CreditCard(customer1.getName(), 1111)

card2 = DebitCard(customer1.getName(), 1234, 200000)

# customer1.addCreditCard(card1)
customer1.addCards(card1)
customer1.addCards(card2)

# for t in tickets:
#     print(t, "\n")
#
# for c in customer1.cards:
#     print(c, "\n")
#
# pos = 0
# buyTicket(tickets[pos], customer1, 1)


def saveFile(fn, data):
    with open(f'load/{fn}.pickle', 'wb') as file:
        print(fn+" saved ")
        pickle.dump(data, file)


def loadFile(fn):
    with open(f'load/{fn}.pickle', 'rb') as file:
        return pickle.load(file)


pickled_cust1 = pickle.dumps(customer1)
unpickled_cust1 = pickle.loads(pickled_cust1)
#
# customer1.cardsToString()

# print(customer1.getCards())

# print(f"\n{pickled_cust1}\n")
print(f"\n{unpickled_cust1.getCards()}\n")


