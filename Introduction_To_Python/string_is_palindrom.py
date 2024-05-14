# Create a Python function to check if a given string is a palindrome

################ Code ################################

def is_palindrome(string):
    # Remove whitespace and convert to lowercase
    string = string.replace(" ", "").lower()
    
    # Check if the string is the same as its reverse
    return string == string[::-1]

# Ask the user to enter a string
user_string = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(user_string):
    print(f"{user_string} is a palindrome!")
else:
    print(f"{user_string} is not a palindrome.")
