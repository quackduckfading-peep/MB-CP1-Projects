# Ren Brown, 1, Shopping List Manager

shopping = []
while True:
    action = input("Please choose one of the three options shown: Add, Remove, View, or Exit: ").strip().lower()

    if action == "add":
        item = input("What would you like to add? ")
        shopping.append(item)

    elif action == "remove":
        gone = input("What would you like to remove? ")
        shopping.remove(gone)

    elif action == "view":
        shopping.sort()
       print(*shopping)
         
    elif action == "exit":
        break

    else:
        print("That is not a viable action. Please try again.")