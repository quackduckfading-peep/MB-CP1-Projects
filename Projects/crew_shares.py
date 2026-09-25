# Ren Brown, Crew Shares

import random

p = int(input(f"How many pirates are there? "))

pirates = (p + 2)

units = random.randint(500, 5000)

print(f"We found {units} units!")

givin = (p * 3)

galactic = round(units - givin)

print(f"They gave the crew three coins each. They now have {galactic} units.")

yondu = round(galactic * 0.13)

pete = round(galactic - yondu)

print(f"Yondu took {yondu} units.")

peter = round(pete * 0.11)

crew = round(pete - peter)

print(f"Peter takes {peter} units.")

share = (crew / pirates)

print(f"The crew gets {share} units.")

yonyon = (yondu + share)
quill = (peter + share)