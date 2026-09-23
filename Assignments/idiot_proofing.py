# Ren Brown, Idiot Proof

while True:
    try:
        name = input("What is your name: ").strip().title()
    except:
        print("That is also not a letter or name.")

while True:
    try:
        phone_numbr = int(input("What is your phone number: "))
    except:
        print("That is not a phone number or a number. Try again.")
    else:
        break

while True:
    try:
        gpa = float(input("What is your GPA "))
    except:
        print("That's not a valid number. Don't be an idiot.")
    else:
        break

    gpa = str(gpa)