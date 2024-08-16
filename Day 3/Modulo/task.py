while True:
    number_input = int(input("Write any number to check weather it is a odd or even number\n"))
    if number_input % 2 == 0:
        print("Given number is Even")
    else:
        print("Given number is Odd")

    while True:

        next_round =input("Do you want to test another number as well?  Type ('Yes' or 'No') ")
        if next_round.lower() == "yes":
            break
        elif next_round.lower()=="no":
            exit()
        else:
            print("Invalid input please type (yes or no)")
            continue

