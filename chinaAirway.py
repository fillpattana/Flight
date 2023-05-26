from airway import *
from boeing777 import *


class chinaAirway(airway):
    destination = ["United States", "United Kingdom", "United Arab Emirates", "Hong Kong", "Turkey",
                   "Thailand", "Taiwan", "Switzerland", "Spain", "South Africa", "Singapore", "Russia",
                   "Papua New Guinea", "Pakistan", "Norway", "Nigeria", "New Zealand", "Morocco",
                   "Malaysia", "South Korea", "Jordan", "Japan", "Italy", "Indonesia",
                   "India", "Guinea", "Germany", "France", "Egypt", "Denmark", "Czech Republic", "Cuba",
                   "Colombia", "China", "Canada", "Cambodia", "Myanmar", "Belgium", "Bangladesh",
                   "Austria", "Australia", "Afghanistan"]

    def __init__(self):
        self.planes = boeing777()

    def flyTo(self, country):
        if country in self.destination:
            return True
        else:
            return False

    def getAirway(self):
        return "ChinaAirway"

    def getDestination(self):
        return self.destination

    def getAirplane(self):
        return self.planes

    def getSeats(self):
        return self.planes.getNumSeats()

    def getEconomyPricing(self, km):
        if km <= 1500:
            return 1.80
        elif km <= 4500:
            return 2.40
        else:
            return 2.80

    def getBusinessPricing(self, km):
        if km <= 1500:
            return 2.8
        elif km <= 4500:
            return 3.4
        else:
            return 4.8

    def getFirstClassPricing(self, km):
        if km <= 1500:
            return 3.3
        elif km <= 4500:
            return 3.9
        else:
            return 5.3

    def getLoadWeight(self):
        return 30

    def allowPets(self):
        return False

