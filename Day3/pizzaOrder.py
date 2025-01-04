print("Welcome to Python Pizza Deliveries!")
bill = 0

size = input("What size pizza do you wnat? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y ir N: ")

if size == "S" or "s":
    bill = bill + 15
    print("The cost of pizza is $15.")
elif size == "M" or "m":
    bill = bill + 20
    print("The cost of pizza is $20.")
elif size == "L" or "l":
    bill = bill + 25
    print("The cost of pizza is $25.")

if add_pepperoni == "Y" or "y":
    if size == "S" or "s":
        bill = bill + 2
    else:
        bill = bill + 3

if extra_cheese == "Y" or "y":
    bill = bill + 1
    print(f"Your final bill is ${bill}.")