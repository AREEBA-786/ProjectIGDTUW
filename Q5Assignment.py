# Writing the input to the text file
user_input = input("Enter a string: ")
file_name = "result.txt"
file = open(file_name, "w")
file.write(user_input)
file.close()

print("The string has been written to", file_name)
