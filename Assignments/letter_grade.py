# Ren Brown, 1, What is My Grade

grade = input("What is your grade: ")

if grade > 93:
    print(f"Your percentage grade is {grade}")
    print("Your grade is an A. Good job!")
elif grade >= 80:
    print(f"Your percentage grade is {grade}")
    print("You have a B.")

elif grade < 60:
    print(f"Your percentage grade is {grade}")
    print("Your grade is an F.")