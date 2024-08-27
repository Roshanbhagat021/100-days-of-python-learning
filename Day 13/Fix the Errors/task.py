try:
    age = int(input("How old are you? "))
except ValueError:
    print("Invalid input please write your age in numerical value like 20")
    age = int(input("How old are you? "))

if age > 18:
   print(f"You can drive at age {age}.")
else:
    print(f"Hey kid go and play with toys alright!!")
