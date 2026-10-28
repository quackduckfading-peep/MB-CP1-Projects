# Ren Brown, 1, Password Strength Checker Code

password = input("Please make a password: ")

beep = str(password)

points = 0

if len(beep) >= 8:
    points += 1
    print(f"Length 8+ characters: YES ")
else:
    print(f"Length 8+ characters: NO")

"""for character in beep:
    if character.isupper():
        points += 1
        print(f"Contains uppercase: YES")
        break
    else:
        print("Contains uppercase: NO")
        break"""

for letter in beep:
    if any(letter.islower()):
        points += 1
        print("Contains lowercase: YES")
        break
    else:
        print("Contains lowercase: NO")
        break