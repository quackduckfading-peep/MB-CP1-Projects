# Ren Brown, Debug with the Debugger

# Ravager Snack Bar
import random

pirate_name = input("What's your name, space pirate? ") #I hate normal pirates so this is a space pirate.
snack_name = input("What snack do you want? ")

price = random.randint(2, 8)  # random price in credits
quantity = int(input("How many would you like? ")) #changed it to do my bidding (i just changed it to integers)

total = price * quantity

discounted_total = int(total - 7.0 * 0.10)

tax_rate = 0.08
total_with_tax = discounted_total + (discounted_total * tax_rate)

print("Hello, " + pirate_name + "! Here's your order summary:")
print("Snack: " + snack_name)  #the variable was spelled wrong
print("Price per snack: " + str(price) + " credits")
print("Total before tax: " + str(discounted_total)) #it was price but price doesn't give us a discounted total
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits")