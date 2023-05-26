from americanAirway import *
from chinaAirway import *
from emiratesAirway import *
from singaporeAirway import *
from thaiAirways import *

AmericanAirway = americanAirway()
ChinaAirway = chinaAirway()
EmiratesAirway = emiratesAirway()
SingaporeAirway = singaporeAirway()
ThaiAirway = thaiAirways()

defaultAirways = [AmericanAirway, ChinaAirway, EmiratesAirway, SingaporeAirway, ThaiAirway]


def getAvailableAirway(arrival, departure):
    result = []
    for defaultAirway in defaultAirways:
        if defaultAirway.flyTo(arrival) and defaultAirway.flyTo(departure):
            result.append(defaultAirway)
    return result


def generateBusinessPrice():
    pass


def generateFirstPrice():
    pass


def generateEconomyPrice():
    pass


# a = getAvailableAirway("Thailand", "Cambodia")
# print(a)




# here = "Thailand"
# des = "Argentina"
# airways = [AmericanAirway, ChinaAirway, EmiratesAirway, SingaporeAirway, ThaiAirway]
# for airway in airways:
#     if airway.flyTo(des):
#         print("I am " + airway.getAirway() + "And I go to " + des)
#     else:
#         print("I am " + airway.getAirway() + "And I don't go to " + des)

# print(airway.getDistance(here, des))


# x = datetime.datetime.now()
# print(x.month)
# print(x.strftime("%A"))




