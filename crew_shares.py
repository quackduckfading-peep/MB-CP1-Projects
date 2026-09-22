# Ren Brown, Crew Shares

import random

p = int(input(f"How many pirates are there? "))

pirates = (p + 2)

units = random.randint(500, 5000)

print(f"We found {units} units!")

givin = (p * 3)

galactic = (units - givin)

print(f"They gave the crew three coins each. They now have {galactic} units.")