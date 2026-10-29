# Ren Brown, 1, Password Strength Checker Code

password = input("Please make a password: ")

beep = list(password)

points = 0

if len(beep) >= 8:
    points += 1
    print(f"Length 8+ characters: YES ")
else:
    print(f"Length 8+ characters: NO")

for i in beep:
    if (i.isupper()):
        points += 1
        print("Contains uppercase: YES")
        break
    else:
        points += 0

for char in beep:
    if (char.islower()):
        points += 1
        print("Contains lowercase: YES")
        break
    else:
        points += 0

for bop in beep:
    if (bop.isdigit):
        points += 1
        print("Contains number(s): YES")
        break
    else:
        points += 0

for j in beep:
    if (j.isalnum):
        points += 1
        print("Contains special character: YES")
        break
    else:
        points += 0

print(points)