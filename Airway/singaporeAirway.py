import airway


class singaporeAirway(airway):
    destination = ["Florida", "California","Canada", "Hawaii", "Mexico",
                   "Bangkok", "Beijing", "London", "Paris", "Singapore", "Malaysia", "Indonesia"
                    "Dubai", "Japan", "Korea"]

    departures = ["Florida", "California","Canada", "Hawaii", "Mexico",
                   "Bangkok", "Beijing", "London", "Paris", "Singapore", "Malaysia", "Indonesia"
                    "Dubai", "Japan", "Korea"]

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