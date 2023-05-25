import airway


class emiratesAirway(airway):
    destination = ["California", "Arizona", "Bangkok", "Indonesia", "Beijing",
                    "Malaysia", "Japan", "Korea", "Indonesia", "Dubai",
                   "London", "Paris", "Glasgow", "Switzerland", "Australia", "Egypt", "Iran", "Morocco",
                   "Russia", "Jordan", "Turkey"]

    departures = ["California", "Arizona", "Indonesia", "Beijing",
                    "Malaysia", "Japan", "Korea", "Dubai",
                   "London", "Paris", "Egypt", "Iran", "Morocco",
                   "Russia", "Jordan", "Turkey"]

    def getDestination(self):
        return self.destination

    def getDeparture(self):
        return self.departures

    def getAirplane(self):
        pass

    def getSeats(self):
        pass

    def getEconomyPricing(self):
        pass

    def getBusinessPricing(self):
        pass

    def getFirstClassPricing(self):
        pass

    def getCarryOnWeight(self):
        pass

    def getLoadWeight(self):
        pass

    def allowPets(self):
        pass