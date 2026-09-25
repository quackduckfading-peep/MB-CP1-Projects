# Ren Brown, 1, user Sign In

username = input("What is your username: ")
password = input("What is your password: ")

if username == "LaRose":
    if password == "TeAtChEr":
        print("Congratulations, you are signed in!")
        print("Moving onto the next step.")
    else:
        print("Username or Password are incorrect.")
        print("Is this even the right account for you?")
elif username == "Student":
   #print("Moving onto the next step.")

    if password == "sTuDeNt":
        print("Congratulations, you are signed in!")
#else:
  # print("That is not a valid account. Please try again.")
    else:
        print("Username or Passwoed are incorrect.")
        print("Is this even the right account for you?")

else:
   print("That is not a valid account. Please try again.")