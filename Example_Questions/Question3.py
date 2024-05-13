#  Convert temperature from Celsius to Fahrenheit

#################### Code ###########################

# Create a function to calculate the temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Get input from the user
celsius_temp = float(input("Enter the temperature in Celsius:\n"))

# Convert and display the result
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")