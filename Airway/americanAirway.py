from airway import airway


class americanAirway(airway):

    destination = ["Florida", "California", "Texas", "Hawaii", "Arizona", "Colorado", "Iowa",
                   "Canada", "Hawaii", "Mexico", "Cuba", "Bangkok", "Beijing", "London", "Paris",
                   "Egypt", "Dubai", "Japan", "Korea"]

    departures = ["Florida", "California", "Colorado", "Iowa",
                   "Canada", "Hawaii", "Mexico", "Cuba", "Bangkok", "Beijing", "London", "Paris",
                   "Egypt", "Korea", "Indonesia", "Singapore"]

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


a = americanAirway()
d1 = "Rome"
d2 = "Paris"
print(a.getDistance(d1, d2))

