# Ren Brown, 1, Combat Program

import time

def dirt(classification):
    classification = 1
    if classification == 1:
        hp = 50
        defense = 3
        damage = 100
        cooldown = 3

def stats_dirt(hp, defense, damage, cooldown):
    hp = 50
    defense = 3
    damage = 100
    cooldown = 3
    print(hp)
    print(defense)
    print(damage)
    print(cooldown)

def unfit_human(classification):
    classification = 2
    if classification == 2:
        hp = 25
        defense = 100
        damage = 80
        cooldown = 15

#add stats_human

player = input("What is your name? ")
classification = input("What type of a class are you? Click 1 for Dirt. Click 2 for an unfit human. Click 3 for a tree. Please choose now: ")

if classification == "1":
    hp = dirt(1)
    defense = dirt(1)
    damage = dirt(1)
    cooldown = dirt(1)
    print("Your stats are as follows:")
    stats_dirt(50, 3, 100, 3)
elif classification == "2":
    j


"""elif classification == "2":
    print("Your stats are as follows:")
    print("HP: 25")
    print("Defense: 100")
    print("Damage: 80")
    print("Cooldown: 15 seconds")
elif classification == "3":
    print("HP: 26")
    print("Defense: 33")
    print("Damage: 45")
    print("Cooldown: 5 seconds")"""