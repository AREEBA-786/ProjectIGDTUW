# Performing arithmetic operations based on the operator
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        result = "Division by zero is not allowed"
    else:
        result = num1 / num2
else:
    result = "Invalid operator entered"
print(f"The result of {num1} {operator} {num2} is:", result)
