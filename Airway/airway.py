from abc import ABC, abstractmethod
import pandas as pd
from geopy import distance


class airway(ABC):
    # df = pd.read_csv("/Users/akararatpattanamontri/Documents/FlightSEP/Flight/Airway/concap.csv")
    df.rename(columns={"CountryName": "Country", "CapitalName": "capital", "CapitalLatitude": "lat",
                       "CapitalLongitude": "lon", "CountryCode": "code", "ContinentName": "continent"}, inplace=True)

    def getDistance(self, destination, departure):
        ropa = self.df[self.df["Country"].isin([destination, departure])].reset_index()
        d = distance.distance((ropa.loc[0, "lat"], ropa.loc[0, "lon"]), (ropa.loc[1, "lat"], ropa.loc[1, "lon"]))
        return d.km

    @abstractmethod
    def flyTo(self, country):
        pass

    @abstractmethod
    def getAirway(self):
        pass

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
    def getEconomyPricing(self, km):
        pass

    @abstractmethod
    def getBusinessPricing(self, km):
        pass

    @abstractmethod
    def getFirstClassPricing(self, km):
        pass

    def getCarryOnWeight(self):
        return 12

    @abstractmethod
    def getLoadWeight(self):
        pass

    @abstractmethod
    def allowPets(self):
        pass
