print("Let's figure out the price of your pizza")
HST = 0.13
LABOUR = 0.75
RENT = 1
MATERIALS = 0.5
diameter = float(input("How big do you want the diameter in inches: "))
subtotal = LABOUR + RENT + MATERIALS * diameter
tax = subtotal * HST
total = subtotal + tax
print("Your total is: $", total)