# Opening and reading from the python file
with open('python.txt', 'r') as input_file:
    lines = python_file.readlines()

with open('output.txt', 'w') as output_file:
    for line in lines:
        output_file.write(line)

print("File copied successfully!")
