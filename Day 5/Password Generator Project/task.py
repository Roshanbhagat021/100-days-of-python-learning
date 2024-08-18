import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")

new_password = []

# taking input and adding random n letters to new_password
nr_letters = int(input("How many letters would you like in your password?\n"))
n_random_letters = random.sample(letters, k=nr_letters)
new_password.extend(n_random_letters)


# taking input and adding random n symbols to new_password
nr_symbols = int(input(f"How many symbols would you like?\n"))
n_random_symbols = random.sample(symbols, k=nr_symbols)
new_password.extend(n_random_symbols)


# taking input and adding random n numbers to new_password
nr_numbers = int(input(f"How many numbers would you like?\n"))
n_random_numbers = random.sample(numbers, k= nr_numbers)
new_password.extend(n_random_numbers)


# Generating random sequence of new_password
random.shuffle(new_password)
print(f"Your Password is: {"".join(new_password)}")
