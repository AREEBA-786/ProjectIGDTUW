#reads multiple lines of input from the user until they enter ....then prints all the lines.
lines=[]
print("Enter multiple lines of text. Enter an empty line to finish:")

while True:
    line = input()
    if line == "":
        break
    lines.append(line)
print("\nYou entered the following lines:")
for line in lines:
    print(line)
