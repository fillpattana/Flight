from Airplane.plane import plane
import random


class boeing777(plane):

    def __init__(self):
        self.wingSpan = 64.8
        self.length = 63.7
        self.model = "Boeing777"
        self.maxDistance = 15843
        self.numSeats = 355

    def getWingSpan(self):
        return self.wingSpan

    def getLength(self):
        return self.length

    def getNumSeats(self):
        alphabet = ["A", "B", "C",
                    "D", "E",
                    "F", "G", "H"]

        seats = self.numSeats
        rows = round(seats / 8)
        row = random.randint(1, rows)
        seat = alphabet[random.randint(0, 7)]
        return str(str(row) + seat)

    def getModel(self):
        return self.model

    def getMaxDistance(self):
        return self.maxDistance
