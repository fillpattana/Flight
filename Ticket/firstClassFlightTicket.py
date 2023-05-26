from Ticket.flightTicket import *
# import sys
# sys.path.remove('/Users/akararatpattanamontri/Documents/FlightSEP/Flight/Ticket')
# from flightTicket import *

class firstFlightTicket(flightTicket):
    def __init__(self, Name, Destination, Departure, Seat, Price, Airway, Time, Date):
        super().__init__(Name, Destination, Departure, Seat, Price, Airway, Time, Date)
        self.seatClass = "First Class"

    def getClass(self):
        return self.seatClass

    def __str__(self):
        return ("Passenger Ticket : " + self.airway + "\n" +
                "Seat : " + self.seat + " Class : " + self.seatClass + "\n" +
                "Departure : " + self.departure + " Destination : " + self.destination + "\n"
                "Time : "+ self.time + " Date : " + self.date)
