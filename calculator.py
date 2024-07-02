def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Error: Division by zero!"

def main():
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }

    print("Welcome to Simple Calculator!")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")
    if choice in operations:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"Result: {operations[choice](num1, num2)}")
    else:
        print("Invalid input. Please enter a valid number (1/2/3/4).")

if _name_ == "_main_":
    main()