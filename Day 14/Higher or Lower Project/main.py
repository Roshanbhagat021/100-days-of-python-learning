import random

from game_data import data
from art import  vs, logo
# print(len(data))
A, B =(random.choices(list(range(0,50)), k=2))
print(A, B)

def compare(acc_a, acc_b):
    if acc_a["follower_count"] > acc_b["follower_count"]:
        return "a"
    else:
        return "b"
print(logo)
while True:
    score = 0
    A_influencer = data[A]
    B_influencer = data[B]

    while True:

        print(f"Compare A: {A_influencer["name"]}, a {A_influencer["description"]}, from {A_influencer['country']} ")
        print(vs)
        print(f"Against B: {B_influencer["name"]}, a {B_influencer["description"]}, from {B_influencer['country']} ")

        answer = input("Who has more followers? Type 'A' or 'B'").lower()
        result = compare(A_influencer, B_influencer)

        if answer != result :
            print(f"Sorry! That's wrong final score: {score} ")
            break
        else:
            A_influencer = B_influencer
            B_influencer = random.choice(data)
            score += 1

    play_again = input("Do you want to play again? Type 'Y' else 'N'").lower()
    if play_again != "y":
        exit()



