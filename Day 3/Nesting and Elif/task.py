
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Children tickets are 5$")
        bill=5
    elif age <= 18:
        print("Youth ticket are 7$")
        bill=7
    else:
        print("Adult ticket are 12$.")
        bill=12

    wants_photo=input("Do you want have a photo? type y for Yes and n for No ")
    if wants_photo=="y":
        bill+=3

    print(f"You final bill is ${bill}.")

else:
    print("Sorry you have to grow taller before you can ride.")



