# Checking for the presence of the substring in the main string
main_string = input("Enter the main string: ")
substring = input("Enter the substring: ")
a= False
for i in range(len(main_string) - len(substring) + 1):
    if main_string[i:i + len(substring)] == substring:
        a = True
        break
if a:
    print("The substring is present in the main string.")
else:
    print("The substring is not present in the main string.")
