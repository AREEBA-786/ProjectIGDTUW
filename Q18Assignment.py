#t checks if two strings are anagrams of each other.
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")


string1 = string1.replace(" ", "")
string2 = string2.replace(" ", "")
if len(string1) != len(string2):
    are_anagrams = False
else:
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)
    if sorted_string1 == sorted_string2:
        are_anagrams = True
    else:
        are_anagrams = False
if are_anagrams:
    print("The strings are anagrams of each other.")
else:
    print("The strings are not anagrams of each other.")
