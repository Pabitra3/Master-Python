"""Calculates the sum of all positive numbers in a given list of integers."""
################# Code ##################################################

def sum_positive_numbers(numbers):
    
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total

# Ask the user to enter a list of numbers separated by commas
numbers_str = input("Enter a list of numbers separated by commas: ")

# Convert the input string to a list of integers
numbers_list = [int(num) for num in numbers_str.split(",")]

# Calculate the sum of positive numbers
positive_sum = sum_positive_numbers(numbers_list)

# Print the result
print(f"The sum of positive numbers in the list is: {positive_sum}")