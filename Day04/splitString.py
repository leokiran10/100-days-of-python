# Write a program to select who will pay resturant bill today

import random

names_string = input("Gime me everybody's names, seperated by a comma. ")
names = names_string.split(", ")
# print(names)

x = len(names)
random_choice = random.randint(0, x-1)
selected_person = names[random_choice]
print(f"{selected_person} will pay the bill today!")