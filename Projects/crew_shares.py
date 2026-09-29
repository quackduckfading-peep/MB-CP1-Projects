# Ren Brown, Crew Shares

import random

p = int(input(f"How many space pirates are there? "))

pirates = (p + 2)

units = random.randint(500, 5000)

print(f"We found {units} units!")

givin = (p * 3)

galactic = int(round(units - givin))

print(f"They gave the crew three coins each. They now have {galactic} units.")

yondu = int(round(galactic * 0.13, 2))

pete = int(round(galactic - yondu, 2))

print(f"Yondu took {yondu} units.")

peter = int(round(pete * 0.11, 2))

crew = int(round(pete - peter))

print(f"Peter takes {peter} units.")

share = int(round(crew / pirates, 2))

print(f"The crew gets {share} units.")

yonyon = int(round(yondu + share, 2))
quill = int(round(peter + share, 2))



print(f"There are {pirates} pirates.")
print(f"Units found: {units}")

print(f"After handing out 3 coins to each space pirate, they have: {galactic}")

print(f"Yondu's share: {yonyon} galactic units")
print(f"Peter Quill's share: {quill} galactic units")
print(f"Crew's share: {share}")