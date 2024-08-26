import random
from art import logo

print(logo)
while True:
    num_list = list(range(1, 101))
    levels = ["hard", "easy"]

    print("Welcome to the Number Guessing Game!")
    print("I’m thinking of a number between 1 and 100. Don't worry, it's not one of those existential questions.")

    random_num = random.choice(num_list)
    life = 10
    # print(random_num)  # You can comment this out to keep the number hidden
    while (game_level := input("Choose your difficulty level. Type 'easy' for a leisurely stroll or 'hard' for a rollercoaster ride: ").lower()) not in levels:
        print("Oops! That’s not an option. Try again!")

    if game_level == 'hard':
        life = 5
        print("Oh, going for 'hard'? Someone’s feeling brave!")

    while life > 0:
        print(f"Just so you know, you've got {life} shots at glory left.")
        user_input = int(input("Take a wild guess: "))

        if user_input != random_num and life > 0:
            checking_list = list(range(random_num - 3, random_num + 4))
            if user_input > random_num:
                if user_input in checking_list:
                    print("Close, but no cigar. A bit too high.")
                    
                else:
                    print("Way too high! Did you shoot for the stars?")
                life -= 1
                
            elif user_input < random_num:
                if user_input in checking_list:
                    print("Almost there! Just a tad low.")
                    
                else:
                    print(f"{user_input}? You dug too deep into the ground!")
                life -= 1
                
        elif life == 0:
            print("No more guesses left. Better luck next time, my friend!")
            break
            
        elif user_input == random_num:
            print(f"Congratulations, genius! The number was indeed {user_input}. You should try your hand at mind reading!")
            break
            
    # Ask if the user wants to play again
    continue_or_not = input("Fancy another round of fun? Type 'y' to play again or 'n' to quit while you're ahead: ").lower()
    if continue_or_not == "n":
        print("Thanks for playing! See you next time, if you're brave enough.")
        exit()
