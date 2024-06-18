# Printing the minimum and maximum values in the list
numbers = input("Enter a list of numbers separated by spaces: ").split()
min_value = None
max_value = None
for num in numbers:
    current_num = int(num)
    if min_value is None or current_num < min_value:
        min_value = current_num

    if max_value is None or current_num > max_value:
        max_value = current_num
print(f"The minimum value in the list is: {min_value}")
print(f"The maximum value in the list is: {max_value}")
