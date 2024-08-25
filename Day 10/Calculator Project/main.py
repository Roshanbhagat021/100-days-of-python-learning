from art import  logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations ={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}


def perform(input1):
    for operation in operations:
        print(operation)
    op = None
    while True:
         op = input("Pick an operation: ")
         if len(op) != 1 or op not in operations:
             print("Please choose the correct operation")
         else:
             break
    second_input = float(input("What is the next number?: "))
    result = operations[op](input1, second_input)
    print(f"{input1} {op} {second_input} = {result }")

    do_more = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
    if do_more == "y" :
        return perform(result)

print(logo)
while True:
    f_input = float(input("What is the first number?: "))
    perform(f_input)


