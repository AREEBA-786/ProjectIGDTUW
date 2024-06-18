# Reading the content of the text file and Printing the content to the console
file_name = "result.txt"
file = open(file_name, "r")
content = file.read()
file.close()
print(content)
