import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to the ROCK PAPER SCISSORS Game 😎")
while True:
    items = [rock,paper,scissors]

    users_choice = int(input("Chose between three ! Type 0 for ROCK 1 for PAPER and 2 for SCISSORS \n"))
    if users_choice in [0, 1 , 2]:
        print(items[users_choice])
    else:
        print("Invalid input🙄!! Please provide the number between 0 and 2")
        continue

    computers_choice =  random.randint(0,2)
    print("Computer chose:")
    print(items[computers_choice])

    # if users_choice == 0:
    #     if computers_choice == 0:
    #         print("Draw")
    #     elif computers_choice == 1:
    #         print("You lose")
    #     else:
    #         print("You win")
    #
    # elif users_choice == 1:
    #     if computers_choice == 0:
    #         print("You win")
    #     elif computers_choice == 1:
    #         print("Draw")
    #     else:
    #         print("You lose")
    #
    # else:
    #     if computers_choice == 0:
    #         print("You lose")
    #     elif computers_choice == 1:
    #         print("You win")
    #     else:
    #         print("Draw")

    outcomes = [["Draw","You Lose","You Win"],["You Win","Draw","You Lose"],["You Lose","You Win","Draw"]]
    print(outcomes[users_choice][computers_choice])

    play_again = input("Do you want to play again? Type 1 for YES and 0 for NO \n")
    if play_again == "0":
        exit()
    else:
        continue










