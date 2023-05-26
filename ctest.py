from creditCard import CreditCard
from debitCard import *
from customer import*
from ticketGenerator import *


def buyTicket(ticket, cust, i):
    if isinstance(cust.cards[i], CreditCard) and cust.cards[i].getLimit() > ticket.getPrice():
        cust.cards[i].getLimit() - ticket.getPrice()
        cust.addTicket(ticket)
        print(cust.getTicket().__str__())
    elif isinstance(cust.cards[i], DebitCard) and cust.cards[i].getBalance() > ticket.getPrice():
        cust.cards[i].getBalance() - ticket.getPrice()
        cust.addTicket(ticket)
        print(cust.getTicket(), cust.cards[i].getBalance())
    else:
        return "poor shit"

    print(cust.cards[i].getLimit())
    # print(cust.cards[j].getBalance())

    # ticketprice = ticket.getPrice()
    # print("Chosen Ticket:", ticket.getPrice())
    # print("Customer Balance:", cust.creditCard[i].getLimit())


name = "Kittiphong Thachaphat"
desti = "Bangladesh"
depart = "Japan"
date = datetime.date(2023, 5, 27)
a = getAvailableAirway("Japan", "Bangladesh")
tickets = generateBusinessTicket(name, desti, depart, a, date)

customer1 = customer("Indiana Jay", 87, "jaja", "jeje")
card1 = CreditCard(customer1.getName(), 1111)

card2 = DebitCard(customer1.getName(), 1234, 200000)

# customer1.addCreditCard(card1)
customer1.addCards(card1)
customer1.addCards(card2)

for t in tickets:
    print(t, "\n")

for c in customer1.cards:
    print(c, "\n")

pos = 0
buyTicket(tickets[pos], customer1, 0)


