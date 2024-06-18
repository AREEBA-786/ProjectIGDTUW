#takes a list of numbers and returns their sum.
numbers = input("Enter a list of numbers separated by spaces: ").split()
total_sum = 0
for num in numbers:
    total_sum += int(num)
print("The sum of the numbers is:", total_sum)
