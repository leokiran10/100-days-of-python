# dictionary = {key : value}

programming_dictionary = {
    "Bug": "An error in a program that prepents the program form running as expected.",
    "Function": "A piecr of code that you can easily call over again and again",
}

print(programming_dictionary["Bug"])

# Adding new items to dictonary
programming_dictionary["Loop"] = "The action of doing over again and again"

# Wipe an exisiting dictonary
programming_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A error in a your program"

# Loop through dictionary
for thing in programming_dictionary:
    print(thing)

print(programming_dictionary)