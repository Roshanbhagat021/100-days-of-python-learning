import random
from art import logo
print(logo)
while True:
    num_list = list(range(1,101))
    levels = ["hard", "easy"]

    print("Welcome to the Number Guessing Game!")
    print("I am thinking a number between 1 to 100.")

    random_num = random.choice(num_list)
    life = 10
    # print(random_num)
    while (game_level := input("Choose the difficulty level. Type 'easy' or 'hard': ").lower()) not in levels:
        print("Invalid input")
    if game_level == 'hard':
        life = 5


    while True:
        print(f"You have {life} attempts remaining to guess the number.")
        user_input = int(input("Make a Guess: "))
        if user_input != random_num and life > 0:
            if user_input > random_num:
                print("Too high")
                print(user_input)
                life -= 1
            elif user_input < random_num:
                print("Too low")
                print(user_input)
                life -= 1

        elif life == 0:
            print("You've ran out of guesses, You lose")


        elif user_input == random_num:
            print(f"Hurry you got this! The number was {user_input}")
            break

    continue_or_not = input("Do you want to guess another number ? Type 'y' or 'n'").lower()
    if continue_or_not == "n":
        exit()

