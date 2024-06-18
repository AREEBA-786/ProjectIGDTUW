# Opening the CSV file
with open('data.csv', 'r') as file:
    lines = file.readlines()
for line in lines:
    print(line.strip())  # .strip() removes any trailing newline characters
