# Ren Brown, 1, Fix the Game

import random

scores = []
rounds = 3

print("Welcome to Guess the Number! You'll play 3 rounds.")
print("Each round, try to guess the number in as few tries as possible.\n")

for round_num in range(1, rounds + 1):
    secret_number = 5
    guesses = 0
    found = False

    print(f"--- Round {round_num} ---")

    while found == False:
        guess = int(input("Guess a number between 1 and 20: "))
        guesses = guesses + 1

        if guess == secret_number:   #No colon. Added a colon.
            print(f"Correct! It took you {guesses} guesses.")
            found = True
        elif guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")

    scores.append(guesses)

print("\n--- Game Over ---")
print(f"Your guesses per round: {scores}") #Cancatinated wrong. Turned it into an F-string.

total = 0
for score in scores:
    total = total + score #Uneeded line that messed with the average.

average = total / rounds
print("Your average guesses per round was " + str(average))

best_round = scores[0]
for i in range(rounds): #Didn't check the last round. Changed it so that it does check.
    if scores[i] < best_round:
        best_round = scores[i]

print(f"Your best round took only {best_round} guesses!")