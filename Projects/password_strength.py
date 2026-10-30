# Ren Brown, 1, Password Strength Checker Code

password = input("Please make a password: ") # asks the user for the password

beep = list(password) # rearranges the password givin into a list

points = 0 #points for the later score set to zero

if len(beep) >= 8: #checks if the password is eight or more characters long
    points += 1 # adds a single point if there is eight or more characters
    print(f"Length 8+ characters: YES ") #prints out if there is eight or more characters
else:
    points += 0
    print(f"Length 8+ characters: NO") #prints out if there isn't eight or more characters

for i in beep:
    if (i.isupper()): #checks if there is any uppercase characters in the password
        points += 1 #adds a single point if there is an uppercase character
        print("Contains uppercase: YES") #prints out if there is an uppercase character
        break
    else:
        points += 0 #adds nothing if its not true

for char in beep:
    if (char.islower()): #checks if there is any lowercase characters in the password
        points += 1 # adds a single point if there is a lowercase character
        print("Contains lowercase: YES") #prints out if there is a lowercase character
        break
    else:
        points += 0 #adds nothing if it isn't true

for bop in beep:
    if (bop.isdigit): #checks if there are any numbers in the password
        points += 1 # adds a single point if there is at least a single number
        print("Contains number(s): YES") #prints out if there is a number
        break
    else:
        points += 0 #adds nothing if it isn't true

for j in beep:
    if (j.isalnum): #checks if there are any special characters in the password
        points += 1 # adds a single point if there is at least one special character
        print("Contains special character: YES") #prints if there is a special character
        break
    else:
        points += 0 # adds nothing if it isn't true

if points <= 2: # checks the amount of points
    print("Password Strength: Weak") # prints how strong the password is
elif points == 3: # checks the amount of points
    print("Password Strength: Moderate") # prints how strong the password is
elif points == 4: # checks the amount of points
    print("Password strength: Strong") # prints how strong the password is
elif points == 5: # checks the amount of points
    print("Password Strength: Very strong") # prints how strong the password is

print(f"Strength Score: {points}/5") #prints the points total