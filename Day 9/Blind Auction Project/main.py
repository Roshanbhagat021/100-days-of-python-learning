# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


print("Welcome to the blind bidding app we hope for you happy shopping")

def user_input(dicti):
    name = input("what is your name? ")
    bidding_amount = int(input("What is your bid? $"))
    dicti[name] = bidding_amount

user_details = {}

more_bidders = True
while more_bidders :
    user_input(user_details)
    print("\n"*100)
    go_ahead = True
    while go_ahead:
        next_bidder = input("Are there any other bidders? Type 'yes or 'no'?: ").lower()
        if next_bidder == "yes":
            go_ahead = False
        elif next_bidder == "no":
            more_bidders = False
            go_ahead = False
        else:
            print("Invalid input please write 'yes' or 'no'.")

max_bid = 0
second_hightest_bid = 0
person = ""
for bidder in user_details:
    if user_details[bidder] > max_bid:
        second_hightest_bid = max_bid
        max_bid = user_details[bidder]
        person = bidder

print(user_details)
print(f"The Winner is {person} with ${max_bid-second_hightest_bid} extra bids.")


