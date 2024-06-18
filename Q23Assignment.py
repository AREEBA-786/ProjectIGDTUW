# Performing temperature conversion based on user input
temperature = float(input("Enter the temperature value: "))
unit = input("Enter the unit of temperature (C for Celsius, F for Fahrenheit): ")
if unit == 'C':
    converted_temperature = (temperature * 9/5) + 32
    original_unit = 'Celsius'
    converted_unit = 'Fahrenheit'
elif unit == 'F':
    converted_temperature = (temperature - 32) * 5/9
    original_unit = 'Fahrenheit'
    converted_unit = 'Celsius'
else:
    print("Invalid unit entered. Please enter 'C' or 'F'.")
    converted_temperature = None
if converted_temperature is not None:
    print(f"{temperature} {original_unit} is equal to {converted_temperature:.2f} {converted_unit}.")
