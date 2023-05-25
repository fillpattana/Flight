from Airway.airway import *
from Airplane.airbusA380 import *

class singaporeAirway(airway):
    destination = ["United States", "United Kingdom", "United Arab Emirates", "Ukraine", "Hong Kong",
                   "Thailand", "Taiwan", "Switzerland", "Spain", "South Africa", "Singapore", "Russia",
                   "Papua New Guinea", "Norway", "New Zealand", "Netherlands", "Morocco",
                   "Mexico", "Maldives", "Malaysia", "South Korea", "Jordan", "Japan", "Italy", "Indonesia",
                   "India", "Germany", "France", "Egypt", "Denmark", "Czech Republic", "Cuba",
                   "Colombia", "China", "Canada", "Cambodia", "Myanmar", "Brazil", "Belgium", "Bangladesh",
                   "Austria", "Australia", "Argentina"]

    def __init__(self):
        self.planes = airbusA380()

    def flyTo(self, country):
        if country in self.destination:
            return True
        else:
            return False

    def getAirway(self):
        return "SingaporeAirways"

    def getDestination(self):
        return self.destination

    def getAirplane(self):
        return self.planes

    def getSeats(self):
        return self.planes.getNumSeats()

    def getEconomyPricing(self, km):
        if km <= 1500:
            return 1.60
        elif km <= 4500:
            return 2.1
        else:
            return 2.6

    def getBusinessPricing(self, km):
        if km <= 1500:
            return 2.55
        elif km <= 4500:
            return 3.15
        else:
            return 4.35

    def getFirstClassPricing(self, km):
        if km <= 1500:
            return 4.75
        elif km <= 4500:
            return 5.00
        else:
            return 5.95

    def getLoadWeight(self):
        return 20

    def allowPets(self):
        return True
