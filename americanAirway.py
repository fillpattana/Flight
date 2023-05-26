from airway import *
from airbusA380 import *

# import sys
# sys.path.remove('/Users/akararatpattanamontri/Documents/FlightSEP/Flight/Airway')
# sys.path.remove('/Users/akararatpattanamontri/Documents/FlightSEP/Flight/Airplane')
# from airway import *
# from airbusA380 import *




class americanAirway(airway):
    destination = ["United States", "United Kingdom", "Ukraine",
                   "Thailand", "Taiwan", "Switzerland", "Spain", "South Africa", "Singapore",
                   "Papua New Guinea", "Norway", "Nigeria", "New Zealand", "Netherlands", "Morocco",
                   "Mexico", "Maldives", "Malaysia", "South Korea", "Jordan", "Japan", "Italy", "Indonesia",
                   "India", "Germany", "France", "Denmark", "Czech Republic", "Cuba",
                   "Colombia", "China", "Canada", "Cambodia", "Myanmar", "Brazil", "Belgium",
                   "Austria", "Australia", "Argentina"]

    def __init__(self):
        self.planes = airbusA380()

    def flyTo(self, country):
        if country in self.destination:
            return True
        else:
            return False

    def getAirway(self):
        return "AmericanAirway"

    def getDestination(self):
        return self.destination

    def getAirplane(self):
        return self.planes

    def getSeats(self):
        return self.planes.getNumSeats()

    def getEconomyPricing(self, km):
        if km <= 1500:
            return 1.85
        elif km <= 4500:
            return 2.45
        else:
            return 2.85

    def getBusinessPricing(self, km):
        if km <= 1500:
            return 2.85
        elif km <= 4500:
            return 3.45
        else:
            return 4.85

    def getFirstClassPricing(self, km):
        if km <= 1500:
            return 3.35
        elif km <= 4500:
            return 3.95
        else:
            return 5.35

    def getLoadWeight(self):
        return 40

    def allowPets(self):
        return True

# a = americanAirway()
# d1 = "Thailand"
# d2 = "Cambodia"
# print(a.getDistance(d1, d2))
