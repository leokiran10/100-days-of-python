print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________/
*******************************************************************************''')

print("Welcome to the Treasure Island!")
print("Your mission is to find the treasure.")

print("You're at a cross road. Where do you want to go? Type 'left' or 'right'.")
choice1 = input().lower()

if choice1 == "left":
    print("You have come to lake. There is an island in the lake. Type 'wait' to wait or 'swim' to swim across.")
    choice2 = input().lower()
    if choice2 == "wait":
        print("Welcome to the island. There is a house with 3 doors which one you would choose. 'red' 'yellow' or 'blue'.")
        choice3 = input().lower()
        if choice3 == "yellow":
            print("Congrulations! You found the treasure.")
        else:
            print("Game Over! You entered the wrong room.")


    else:
        print("You are eaten by Crocodiles. Game Over!")
else:
    print("You fell into a hole. Game Over!")

