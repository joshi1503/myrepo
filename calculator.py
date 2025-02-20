def get_number():
    while True:
        num_str = input("Enter a number (or 'exit' to quit): ").strip().lower()
        if num_str == 'exit':
            return None
        try:
            return float(num_str)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operator():
    while True:
        op = input("Enter an operation (+, -, *, /) or 'exit': ").strip().lower()
        if op == 'exit':
            return None
        if op in ['+', '-', '*', '/']:
            return op
        print("Invalid operation. Please enter one of +, -, *, /.")

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero!"
        else:
            return num1 / num2

print("Welcome to the Python Calculator App!")

while True:
    print("\nNew calculation")
    num1 = get_number()
    if num1 is None:
        break
    op = get_operator()
    if op is None:
        break
    num2 = get_number()
    if num2 is None:
        break
    result = calculate(num1, num2, op)
    print(f"Result: {num1} {op} {num2} = {result}")

print("\nThank you for using the calculator. Goodbye!")