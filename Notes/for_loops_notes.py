# RB, For Loops Notes

#Iteration
siblings = ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake", "Michael", "Ella"]

for sibling in siblings:
    print(f"Good morning {sibling}!")


grades = {100, 87, 53, 45, 78, 72, 88, 3, 94}
average = 0

for grade in grades:
    average += grade
    print(f"{grade} was added.")

average = average/len(grades)
print(f"The average grade is {average:.2f}")