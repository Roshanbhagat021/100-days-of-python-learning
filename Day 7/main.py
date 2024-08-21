import random
from art import stages, logo


word_list = [
    "lion", "tiger", "elephant", "giraffe", "zebra", "kangaroo",
    "panda", "bear", "wolf", "fox", "rabbit", "deer", "horse",
    "dog", "cat", "mouse", "rat", "squirrel", "bat", "koala",
    "lemur", "otter", "raccoon", "hippopotamus", "crocodile",
    "alligator", "dolphin", "whale", "shark", "octopus",
    "penguin", "ostrich", "eagle", "falcon", "parrot",
    "peacock", "flamingo", "turkey", "hen", "goose",
    "buffalo", "bison", "donkey", "camel", "cheetah",
    "chimpanzee", "gorilla", "orangutan", "leopard", "jaguar"
]
print(logo)
lives = 6
chosen_word = random.choice(word_list)
# chosen_word = "cat"
print(chosen_word)
display = ["_"]*len(chosen_word)
while lives > 0:
     # print(display)
     if "".join(display) == chosen_word:
         print("You Win! 😎")
         exit()
     guess = input("Guess a animal name and write a letter of it.").lower()
     if guess in chosen_word:
         print(f"You guessed '{guess}' and that's correct🤩")
         for letters_count, letter in enumerate(chosen_word):
             if guess == letter:
                 if display[letters_count] == guess:
                     print(stages[lives])
                     continue
                 else:
                     display[letters_count] = guess
                     print(stages[lives])
                     break

     else:
         lives -= 1
         print(f"{lives} life left")
         print(stages[lives])


     print(*display)

if "".join(display) != chosen_word:
    print("You lose")
else:
    print("You Win!!!😎")





# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
