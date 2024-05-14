"""Converts a given number of days into years, weeks, and days."""
################### Code ##################

# Create a function to convert the days into years, weeks, days
def convert_days(total_days):
    
    years = total_days // 365
    remaining_days = total_days % 365
    weeks = remaining_days // 7
    days = remaining_days % 7
    return years, weeks, days

# Get input from the user
total_days = int(input("Enter the number of days: "))

# Convert the days into years, weeks, and days
years, weeks, days = convert_days(total_days)

# Print the result
print(f"{total_days} days is equivalent to {years} years, {weeks} weeks, and {days} days.")