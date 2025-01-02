# Total bill calculator per person adding tip.
print("Welcome to the tip Calculator.")
total_bill = float(input("Whaat was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10,12, or 15?"))
total_people = int(input("How many people to split the bill?"))
bill_adding_tip = tip_percent /100 * total_bill + total_bill
bill_per_person = bill_adding_tip / total_people
final_amount_per_person = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount_per_person}")

