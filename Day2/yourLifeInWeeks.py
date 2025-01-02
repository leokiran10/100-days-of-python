age = input("What is your current age?")

age_in_int = int(age)

years_remaining = 90 - age_in_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining *52
months_remaining = years_remaining * 12

print(f"You hame {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left")