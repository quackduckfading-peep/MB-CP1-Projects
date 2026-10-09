# RB, While Loops

import random
import time

goose = random.randint(1,20)
duck = 1

while goose > duck:
    print("duck...")
    time.sleep(0.3)
    duck += 1
    if duck == 15:
         print("Game over")
         break
    else:
        print("GOOSE!")


count = 1 # or 30

while count <= 30: # or count>= 1:
    print(count)
    time.sleep(0.1)
    count += 1 # or -=


number = random.randint(1,101)

while True:
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess < 0 or guess > 100:
                print("You should read the instructions, stupid!")
                continue
            break
        except:
            print("That isn't a number")
    if guess == number:
                print("You win!")
                break
    elif guess < number:
                 print("That number is too low.")
    elif guess > number:
                 print("That number is too high.")
    else:
        print("I dont know how you got here... but you did something horribly wrong.")