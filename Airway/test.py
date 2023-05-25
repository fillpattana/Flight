import pandas as pd
from geopy import distance

df = pd.read_csv("concap.csv")
df.rename(columns={"CountryName": "Country", "CapitalName": "capital", "CapitalLatitude": "lat",
                   "CapitalLongitude": "lon", "CountryCode": "code", "ContinentName": "continent"}, inplace=True)


destination = "Rome"
Departure = "Paris"
ropa = df[df["capital"].isin([destination, Departure])].reset_index()
d = distance.distance((ropa.loc[0, "lat"], ropa.loc[0, "lon"]), (ropa.loc[1, "lat"], ropa.loc[1, "lon"]))

print(d.km)
