from plane import plane
import random


class airbusA380(plane):
    def __init__(self):
        self.wingSpan = 80
        self.length = 73
        self.model = "Airbus A380"
        self.maxDistance = 15200
        self.numSeats = 720

    def getLength(self):
        return self.length

    def getWingSpan(self):
        return self.wingSpan

    def getNumSeats(self):
        alphabet = ["A", "B", "C",
                    "D", "E", "F",
                    "G", "H", "I"]

        seats = self.numSeats
        rows = round(seats / 9)
        row = random.randint(1, rows)
        seat = alphabet[random.randint(0, 8)]
        return str(str(row) + seat)

    def getModel(self):
        return self.model

    def getMaxDistance(self):
        return self.maxDistance
