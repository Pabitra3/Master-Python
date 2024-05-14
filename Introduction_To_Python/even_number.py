# Write a program to check if a number is even or odd

############## Code ##############################

# Ask the user to enter a number
num = int(input("Enter a number: "))

# Check if the number is even or odd
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")