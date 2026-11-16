# RB, Dictionary

#Collection of key and value pairs.

"""car = {
    "make": "Jeep",
    "model": "Wrangler",
    "color": "silver",
    "year": 2023
}

keys = list(car.keys())
car.pop("colour")
values = list(car.values())
for key in keys:
    print(f"{key} is {car[key]}")

if "transmission" in car:
    print(car["transmission"])
else:
    car["transmission"] = "automatic"
"""

avatar ={
    "water": {
        "Katara": "Water bender",
        "Sokka": "Leader. Boomerang guy. Idea guy. Sword master.",
    },
    "Earth":{
        "Toph": "Earth bender, Blind, The GOAT!",
        "Suki": "Warrior from Kyoshi Island",
        "Cabbage Merchant": "My CABBAGES!!!!!!"
    },
    "Air": {
        "Aang": "Air bender, the Avatar"
    },
    "Fire": {
        "Zuko": "Fire bender, Future fire lord",
        "Iroh": "The actual GOAT. Fire Bender, Dragon of the West",
        "Azula": "Fire lord for 1 hour. Amazing fire bender"
    }
}
print(avatar["Fire"]["Iroh"])
print(avatar.get("Earth").get("Bumi"))