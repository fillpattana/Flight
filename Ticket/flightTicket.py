class flightTicket:
    def __init__(self, Name, Destination, Departure, Seat, Price, Airway, Time, Date):
        self.name = Name
        self.destination = Destination
        self.departure = Departure
        self.seat = Seat
        self.price = Price
        self.airway = Airway
        self.time = Time
        self.date = Date

    def getDestination(self):
        return self.destination

    def getDeparture(self):
        return self.departure

    def getSeatNumber(self):
        return self.seat

    def getPrice(self):
        return self.price

    def getAirway(self):
        return self.airway

    def getTime(self):
        return self.time

    def getDate(self):
        return self.date

    def getName(self):
        return self.name

