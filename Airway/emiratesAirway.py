from Airway.airway import *
from Airplane.airbusA380 import *

class emiratesAirway(airway):
    destination = ["United States", "United Kingdom", "United Arab Emirates", "Ukraine", "Turkey",
                   "Thailand", "Taiwan", "Switzerland", "Spain", "South Africa", "Singapore",
                   "Papua New Guinea", "Pakistan", "Norway", "Nigeria", "Morocco",
                   "Mexico", "Maldives", "Malaysia", "South Korea", "Japan", "Italy", "Indonesia",
                   "India", "Guinea", "Germany", "France", "Egypt", "Denmark", "Czech Republic", "Cuba",
                   "China", "Canada", "Brazil", "Belgium", "Bangladesh",
                   "Austria", "Australia"]

    def __init__(self):
        self.planes = airbusA380()

    def flyTo(self, country):
        if country in self.destination:
            return True
        else:
            return False

    def getAirway(self):
        return "EmiratesAirway"

    def getDestination(self):
        return self.destination

    def getAirplane(self):
        return self.planes

    def getSeats(self):
        return self.planes.getNumSeats()

    def getEconomyPricing(self, km):
        if km <= 1500:
            return 2.25
        elif km <= 4500:
            return 3.0
        else:
            return 3.8

    def getBusinessPricing(self, km):
        if km <= 1500:
            return 4.45
        elif km <= 4500:
            return 5.20
        else:
            return 6

    def getFirstClassPricing(self, km):
        if km <= 1500:
            return 5.0
        elif km <= 4500:
            return 5.75
        else:
            return 6.55

    def getLoadWeight(self):
        return 40

    def allowPets(self):
        return False
