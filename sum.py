def sum_of_numbers(input_numbers):
    return sum(map(int, input_numbers.split()))

numbers_input = input("Enter the Numbers:\n")
print(sum_of_numbers(numbers_input))
