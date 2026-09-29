# Ren Brown, 1, What is My Grade

grade = float(input("What is your percentage grade: "))

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
else:
    print("Go check canvas or something. Or sleep. Both are good.")

print("You are broken regarless since school has not changed over 195 years. You poor poor thing. Go to therapy.")