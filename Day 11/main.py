import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_cards():
    card = random.choice(cards)
    return card

def calculate_score(card_list):
    """Take a list of card and returns the sum of card list"""
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0

    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)

    return sum(card_list)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 😑"
    elif c_score == 0:
        return "Lose, dealer has Blackjack 🙀"
    elif u_score == 0:
        return "You win with Blackjack 😎"
    elif u_score > 21:
        return  "You went over . You Lose 😥"
    elif c_score > 21:
        return "Dealer went over, You Win"
    elif u_score > c_score:
        return "You Win 😎"
    else:
        return "You Lose"


def play_game():
    is_game_over = False

    users_card = random.choices(cards, k=2)
    computers_card = random.choices(cards, k=2)
    user_score = -1
    computer_score = -1

    while not is_game_over:
        user_score = calculate_score(users_card)
        computer_score = calculate_score(computers_card)

        print(f"Your cards: {users_card}, current score: {user_score}")
        print(f"Computer's first card: {computers_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                users_card.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computers_card.append(deal_cards())
        computer_score = calculate_score(computers_card)

    print(f"Your final hand {users_card} , final score {user_score}")
    print(f"Computers final hand {computers_card}, final score {computer_score}")
    print(compare(user_score, computer_score))

print(logo)
while input("Do you want to play the Blackjack game? Type 'y' or 'n'").lower() == "y":
    print("\n"*50)
    play_game()


