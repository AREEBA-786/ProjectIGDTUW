# Converting each character to uppercase (if it's a lowercase letter)
string = input("Enter a string: ")
uppercase_string = ""
for char in string:
    if 'a' <= char <= 'z':
        uppercase_char = chr(ord(char) - 32)
    else:
        uppercase_char = char
    uppercase_string += uppercase_char
print("The string in uppercase is:", uppercase_string)
