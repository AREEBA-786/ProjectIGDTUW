# Printing the string without punctuation
string = input("Enter a string with punctuation: ")
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
string_without_punctuation = ""
for char in string:
    if char not in punctuation:
        string_without_punctuation += char
print("String without punctuation:")
print(string_without_punctuation)
