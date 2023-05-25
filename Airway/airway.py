from abc import ABC, abstractmethod
import pandas as pd
from geopy import distance


class airway(ABC):
    df = pd.read_csv("concap.csv")
    df.rename(columns={"CountryName": "Country", "CapitalName": "capital", "CapitalLatitude": "lat",
                       "CapitalLongitude": "lon", "CountryCode": "code", "ContinentName": "continent"}, inplace=True)

    def getDistance(self, destination, departure):
        ropa = self.df[self.df["capital"].isin([destination, departure])].reset_index()
        d = distance.distance((ropa.loc[0, "lat"], ropa.loc[0, "lon"]), (ropa.loc[1, "lat"], ropa.loc[1, "lon"]))
        return d.km

    @abstractmethod
    def getDestination(self):
        pass

    @abstractmethod
    def getDeparture(self):
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
