# Ren Brown, Dice Roller

import random

while True:
    try:
        dice = input(f"I have: D4, D6, D6, D8, D10, D12, and a D20 dice. Choose one please: D")
    except:
        print("That was not an option I gave you. Try again.")
    else:
        break



d4 = random.randint(1,4)
d6 = random.randint(1,6)
d8 = random.randint(1,8)
d10 = random.randint(1,10)
d12 = random.randint(1,12)
d20 = random.randint(1,20)

if dice == 4:
    print(f"You rolled a {d4}.")
if dice == 6:
    print(f"You rolled a {d6}.")
if dice == 8:
    print(f"You rolled a {d8}.")
if dice == 10:
    print(f"You rolled a {d10}.")
if dice == 12:
    print(f"You rolled a {d12}.")
if dice == 20:
    print(f"You rolled a {d20}.")