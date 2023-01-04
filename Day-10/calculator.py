from art import logo

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)
    
    num1 = float(input("Enter your first number: "))

    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operator = input("Pick an operation: ")
        num2 = float(input("Enter your second number: "))
        calculate_function = operations[operator]
        answer = calculate_function(num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")
        ask = input(f"If you want to continue with {answer} as num1? type'y' to continue or type 'n' to end: ")
        if ask == 'y':
            num1 = answer
        else:
            should_continue = False
            print("Goodbye!")
            
calculator()
    
    