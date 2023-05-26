from abc import ABC, abstractmethod


class plane(ABC):
    @abstractmethod
    def getNumSeats(self):
        pass

    @abstractmethod
    def getModel(self):
        pass

    @abstractmethod
    def getMaxDistance(self):
        pass

    @abstractmethod
    def getLength(self):
        pass

    @abstractmethod
    def getWingSpan(self):
        pass