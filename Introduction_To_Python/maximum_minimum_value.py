# Given a list of numbers, find the maximum and minimum values

################ Code #####################################

# Ask the user to enter a list of numbers separated by commas
numbers_str = input("Enter a list of numbers separated by commas: ")

# Convert the input string to a list of integers (Here using the list comprehension for short the code length)
numbers = [int(num) for num in numbers_str.split(",")]

# Find the maximum value
max_value = max(numbers)
print(f"The maximum value in the list is: {max_value}")

# Find the minimum value
min_value = min(numbers)
print(f"The minimum value in the list is: {min_value}")