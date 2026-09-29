# Ren Brown, Crew Shares

import random

p = int(input(f"How many space pirates are there, not including Yondu and Peter: "))

pirates = (p + 2)

units = random.randint(500, 5000)

print(f"We found {units} units!")

givin = (p * 3)

galactic = round(units - givin, 2)

print(f"They gave the crew three coins each. They now have {galactic} units.")

yondu = round(galactic * 0.13, 2)

pete = round(galactic - yondu, 2)

print(f"Yondu took {yondu} units.")

peter = round(pete * 0.11, 2)

crew = round(pete - peter)

print(f"Peter takes {peter} units.")

share = round(crew / pirates, 2)

print(f"The crew gets {share} units.")

yonyon = round(yondu + share, 2)
quill = round(peter + share, 2)


print(f"Yondu's share: {yonyon:.2f} galactic units")
print(f"Peter Quill's share: {quill:.2f} galactic units")
print(f"Crew's share: {share:.2f}")