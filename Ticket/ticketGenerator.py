# from Airway.test import getAvailableAirway
from Ticket.flightTicket import *
from Ticket.firstClassFlightTicket import *
from Ticket.businessFlightTicket import *
from Ticket.economyFlightTicket import *
from Airway.americanAirway import *
from Airway.chinaAirway import *
from Airway.emiratesAirway import *
from Airway.singaporeAirway import *
from Airway.thaiAirways import *
import datetime
import random

AmericanAirway = americanAirway()
ChinaAirway = chinaAirway()
EmiratesAirway = emiratesAirway()
SingaporeAirway = singaporeAirway()
ThaiAirway = thaiAirways()

defaultAirways = [AmericanAirway, ChinaAirway, EmiratesAirway, SingaporeAirway, ThaiAirway]


def getAvailableAirway(arrival, departure):
    result = []
    for defaultAirway in defaultAirways:
        if defaultAirway.flyTo(arrival) and defaultAirway.flyTo(departure):
            result.append(defaultAirway)
    return result


def generateBusinessTicket(Name, Destination, Departure, Airway, Date):
    ticket = []
    for air in Airway:
        dist = air.getDistance(Destination, Departure)
        pricing = air.getBusinessPricing(dist)
        dateDifference = Date.day - datetime.datetime.now().day
        if dateDifference <= 3:
            datePremium = random.uniform(1.55, 1.75)
        elif dateDifference <= 10:
            datePremium = random.uniform(1.25, 1.35)
        else:
            datePremium = random.uniform(1.00, 1.175)

        TicketPrice = round(datePremium * (dist * pricing))
        seat = air.getSeats()
        m = random.randint(0, 60)
        h = random.randint(0, 24)
        ts = f'{h}:{m}'
        obj = businessFlightTicket(Name, Destination, Departure, seat, TicketPrice, air.getAirway(), ts, Date)
        ticket.append(obj)

    return ticket


def generateFirstClassTicket(Name, Destination, Departure, Airway, Date):
    pass


def generateEconomyTicket(Name, Destination, Departure, Airway, Date):
    pass


name = "Kittiphong Thachaphat"
desti = "Bangladesh"
depart = "Japan"
date = datetime.date(2023, 5, 27)
a = getAvailableAirway("Japan", "Bangladesh")
tickets = generateBusinessTicket(name, desti, depart, a, date)

for t in tickets:
    print(t)
    print("\n")

