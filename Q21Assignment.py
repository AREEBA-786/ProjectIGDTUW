#counts the occurrences of a specific element in a list
numbers = input("Enter a list of numbers separated by spaces: ").split()
element = input("Enter the element to count: ")
count = 0
for num in numbers:
    if num == element:
        count += 1
print(f"The element '{element}' occurs {count} time in the list.")
