from Ticket.flightTicket import *
# import sys
# sys.path.remove('/Users/akararatpattanamontri/Documents/FlightSEP/Flight/Ticket')
# from flightTicket import *

class businessFlightTicket(flightTicket):
    def __init__(self, Name, Destination, Departure, Seat, Price, Airway, Time, Date):
        super().__init__(Name, Destination, Departure, Seat, Price, Airway, Time, Date)
        self.seatClass = "Business Class"

    def getClass(self):
        return self.seatClass

    def __str__(self):
        return ("Passenger Name : " + str(self.name) + " | Passenger Ticket : " + str(self.airway) + "\n" +
                "Seat : " + str(self.seat) + " | Class : " + str(self.seatClass) + "\n" +
                "Departure : " + str(self.departure) + " | Destination : " + str(self.destination) + "\n"
                "Time : "+ str(self.time) + " | Date : " + str(self.date) + " | Price : " + str(self.price))

