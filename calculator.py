import os
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

operations_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    number1=float(input("Enter first number:"))
    for symbol in operations_dict:
        print(symbol)

    continue_flag=True
    while continue_flag:
        op_symbol=input("Pick an operator:")
        number2=float(input("Enter next number:"))
        calculator_func=operations_dict[op_symbol]
        output=calculator_func(number1,number2)
        print(f"{number1} {op_symbol} {number2} = {output}")
        to_continue=input(f"Enter 'y' to continue with {output} or 'n' to new  or 'x' to exit :").lower()
        if to_continue=='y':
            number1=output
        elif to_continue=='n':
            continue_flag=False
            os.system('cls')
            calculator()
        else:
            continue_flag=False
            print("Thanks")
calculator()

