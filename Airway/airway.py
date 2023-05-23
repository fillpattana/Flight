from abc import ABC, abstractmethod


class airway(ABC):
    @abstractmethod
    def getDestination(self):
        pass

    @abstractmethod
    def getAirplane(self):
        pass

    @abstractmethod
    def getSeats(self):
        pass

    @abstractmethod
    def getEconomyPricing(self):
        pass

    @abstractmethod
    def getBusinessPricing(self):
        pass

    @abstractmethod
    def getFirstClassPricing(self):
        pass

    @abstractmethod
    def getCarryOnWeight(self):
        pass

    @abstractmethod
    def getLoadWeight(self):
        pass

    @abstractmethod
    def allowPets(self):
        pass
