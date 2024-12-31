print("Welcome to Rollercoaster program !")
height = int(input("please enter your height (in cms): "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster !")
    age = int (input("please enter your age : "))
    if 12 < age < 18:
        bill = 7
        print("Child tickets are $7")
    elif age < 12:
        bill = 5
        print("Youth tickets are $5")
    elif age >= 45 and age <=55:
        print("Everything is going to be okay, Have a free ride on us !")
    else:
        bill = 12
        print("Adult tickets are $12")
        
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
        
    print(f"Your final bill is ${bill}")
            
else:
    print("Sorry, you have to be over 120 cms tall to ride the rollercoaster")
