from airway import *
from boeing777 import *


class thaiAirways(airway):
    destination = ["United States", "United Kingdom", "United Arab Emirates", "Ukraine", "Hong Kong", "Turkey",
                   "Thailand", "Taiwan", "Switzerland", "Spain", "South Africa", "Singapore", "Russia",
                   "Papua New Guinea", "Pakistan", "Norway", "Nigeria", "New Zealand", "Netherlands", "Morocco",
                   "Mexico", "Maldives", "Malaysia", "South Korea", "Jordan", "Japan", "Italy", "Indonesia",
                   "India", "Guinea", "Germany", "France", "Egypt", "Denmark", "Czech Republic", "Cuba",
                   "Colombia", "China", "Canada", "Cambodia", "Myanmar", "Brazil", "Belgium", "Bangladesh",
                   "Austria", "Australia", "Argentina", "Afghanistan"]

    def __init__(self):
        self.planes = boeing777()

    def flyTo(self, country):
        if country in self.destination:
            return True
        else:
            return False

    def getAirway(self):
        return "ThaiAirway"

    def getDestination(self):
        return self.destination

    def getAirplane(self):
        return self.planes

    def getSeats(self):
        return self.planes.getNumSeats()

    def getEconomyPricing(self, km):
        if km <= 1500:
            return 1.815
        elif km <= 4500:
            return 2.325
        else:
            return 2.795

    def getBusinessPricing(self, km):
        if km <= 1500:
            return 2.556
        elif km <= 4500:
            return 3.288
        else:
            return 4.12

    def getFirstClassPricing(self, km):
        if km <= 1500:
            return 3.915
        elif km <= 4500:
            return 4.125
        else:
            return 4.955

    def getLoadWeight(self):
        return 30

    def allowPets(self):
        return True
