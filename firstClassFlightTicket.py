from flightTicket import *
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
        return ("Passenger Ticket :\t" + str(self.airway) + "\n" + "\nPassenger Name :\t" + str(self.name) +
                "\nSeat :\t" + str(self.seat) + "\tClass :\t" + str(self.seatClass) + "\n" +
                "Departure :\t\t" + str(self.departure) + "\nDestination :\t\t" + str(self.destination) + "\n"
                                                                                                          "Time :\t" + str(
                    self.time) + "\tDate :\t" + str(self.date) + "\nPrice :\t\t" + str(self.price))
