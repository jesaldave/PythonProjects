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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1=input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\".")
if choice1 == "right":
    print("You fell into a hole. Game Over.")
elif choice1 == "left":
    choice2=input("You came across a lake, do you want to swim or wait for a boat ? Type 'swim' or 'wait'.")
    if choice2 == "swim":
        print("You got attacked by a trout. Game Over.")
    elif choice2 == "wait":
        print("You wait for a boat and a boat arrives, you safely reach a mysterious island...")
        choice3=input("You see 3 doors in front of you, which one do you wanna choose ? Type 'red', 'yellow' or 'blue'.")
        if choice3 == "red":
                print("You got into a room full of lava and got burned. Game Over.")
        elif choice3 == "blue":
                print("You got into a room full of beasts and get eaten. Game Over.")
        elif choice3 == "yellow":
                print("You chose the correct door, You Win !")
        else:
                print("Wrong input, Game Over")
                    
