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
    ticket = []
    for air in Airway:
        dist = air.getDistance(Destination, Departure)
        pricing = air.getFirstClassPricing(dist)
        dateDifference = Date.day - datetime.datetime.now().day
        if dateDifference <= 3:
            datePremium = random.uniform(1.65, 1.85)
        elif dateDifference <= 10:
            datePremium = random.uniform(1.35, 1.45)
        else:
            datePremium = random.uniform(1.10, 1.375)

        TicketPrice = round(datePremium * (dist * pricing))
        seat = air.getSeats()
        m = random.randint(0, 60)
        h = random.randint(0, 23)
        ts = f'{h}:{m}'
        obj = firstFlightTicket(Name, Destination, Departure, seat, TicketPrice, air.getAirway(), ts, Date)
        ticket.append(obj)

    return ticket


def generateEconomyTicket(Name, Destination, Departure, Airway, Date):
    ticket = []
    for air in Airway:
        dist = air.getDistance(Destination, Departure)
        pricing = air.getEconomyPricing(dist)
        dateDifference = Date.day - datetime.datetime.now().day
        if dateDifference <= 3:
            datePremium = random.uniform(1.315, 1.525)
        elif dateDifference <= 10:
            datePremium = random.uniform(1.015, 1.125)
        else:
            datePremium = random.uniform(1.05, 1.075)

        TicketPrice = round(datePremium * (dist * pricing))
        seat = air.getSeats()
        m = random.randint(0, 60)
        h = random.randint(0, 24)
        ts = f'{h}:{m}'
        obj = economyFlightTicket(Name, Destination, Departure, seat, TicketPrice, air.getAirway(), ts, Date)
        ticket.append(obj)

    return ticket


def generateTicket(passengerName, destination, departure, daydate, classtype):
    availableAirway = getAvailableAirway(departure, destination)
    if classtype == "Business":
        tickets = generateBusinessTicket(passengerName, destination, departure, availableAirway, daydate)
    elif classtype == "FirstClass":
        tickets = generateFirstClassTicket(passengerName, destination, departure, availableAirway, daydate)
    else:
        tickets = generateEconomyTicket(passengerName, destination, departure, availableAirway, daydate)

    return tickets


name = "Kittiphong Thachaphat"
desti = "Thailand"
depart = "Japan"
date = datetime.date(2023, 5, 27)
tickettype = "Economy"
tic = generateTicket(name, desti, depart, date, tickettype)

for t in tic:
    print(t)
    print("\n")
