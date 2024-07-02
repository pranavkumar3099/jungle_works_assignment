def divide_numbers():
    try:
        a = float(input("Enter the numerator: "))
        b = float(input("Enter the denominator: "))
        result = a / b
    except ValueError:
        print("Error: Please enter a valid number")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"The result of {a} divided by {b} is {result}")
    finally:
        print("Execution completed")

# Example usage:
divide_numbers()