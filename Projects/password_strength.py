# Ren Brown, 1, Password Strength Checker Code

password = input("Please make a password: ")

beep = list(password)

points = 0

if len(beep) >= 8:
    points += 1

for i in beep:
    if beep.isupper():
        return True
    return False
    