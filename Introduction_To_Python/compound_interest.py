""" Calculates the compound interest for a given principal amount, interest rate, and time period """

def compound_interest(principal, rate, time):
    
    amount = principal * (1 + rate) ** time
    interest = amount - principal
    return interest

# Get input from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (e.g., 0.05 for 5%): "))
time = int(input("Enter the time period in years: "))

# Calculate the compound interest
interest = compound_interest(principal, rate, time)

# Print the compound interest
print(f"Compound interest: ${interest:.2f}")