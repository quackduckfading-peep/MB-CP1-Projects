# Ren Brown, 1, What is My Grade

grade = int(input("What is your grade: "))

if grade >= 93:
    print(f"Your percentage grade is {grade}")
    print("Your grade is an A. Good job!")
elif grade >= 80:
    print(f"Your percentage grade is {grade}")
    print("You have a B.")
elif grade >= 70:
    print(f"Your percentage grade is {grade}")
    print("You have a C.")
elif grade >= 60:
    print(f"Your percentage grade is {grade}")
    print("You have a D")
elif grade <= 59:
    print(f"Your percentage grade is {grade}")
    print("Your grade is an F.")