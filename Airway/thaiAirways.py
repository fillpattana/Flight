import airway


class thaiAirways(airway):
    destination = ["California", "Arizona", "Bangkok", "Indonesia", "Beijing", "ShiangHai",
                   "Canada", "Hawaii", "Mexico", "Malaysia", "Japan", "Korea", "Indonesia", "Dubai",
                   "London", "Paris", "Glasgow", "Switzerland", "Australia"]

    departures = ["California", "Bangkok", "Indonesia", "Beijing", "ShiangHai",
                  "Canada", "Hawaii", "Malaysia", "Japan", "Korea", "Indonesia", "Dubai",
                  "London", "Paris", "Australia"]

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