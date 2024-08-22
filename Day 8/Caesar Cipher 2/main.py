from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter == " " or not letter.isalpha():
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")



def decrypt(original_text, shift_amount):
    decoded_text = ""
    for letter in original_text:
        if letter == " " or not letter.isalpha():
            decoded_text += letter
        else:
            shifted_position = alphabet.index(letter) - shift_amount
            decoded_text += alphabet[shifted_position]
    print(f"Here is the decoded result of {original_text}: {decoded_text}")


def caesar():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != "encode" and direction != "decode":
        print("Invalid input please choose one of these two: encode or decode")
        return  caesar()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt(original_text=text, shift_amount=shift)
    elif direction == "decode":
        decrypt(original_text=text, shift_amount=shift)





print(logo)
while True:
    caesar()
    play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if play_again.lower() == "yes":
        continue
    else:
        print("Ok Bye")
        exit()





