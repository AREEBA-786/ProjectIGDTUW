#  converts a given string to title case (first letter of each word capitalized).
string = input("Enter a string: ")
start_of_word = True
title_case_string = ""

for char in string:
    if start_of_word:
        title_case_string += char.upper()
        start_of_word = False
    else:
        title_case_string += char
    if char == ' ':
        start_of_word = True
print("The string in title case is:", title_case_string)
