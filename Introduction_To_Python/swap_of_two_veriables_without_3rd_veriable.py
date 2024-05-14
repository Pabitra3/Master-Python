#  Implement a program that swaps the values of two veriables

#################### Code ####################################

# Get input from the user
var1 = input("Enter the value of the first variable: ")
var2 = input("Enter the value of the second variable: ")

# Print the original values
print("Original values:")
print(f"Variable 1: {var1}")
print(f"Variable 2: {var2}")

# Swap the values using tuple assignment
var1, var2 = var2, var1


# Print the swapped values
print("\nSwapped values:")
print(f"Variable 1: {var1}")
print(f"Variable 2: {var2}")