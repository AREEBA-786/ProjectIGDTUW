# checks if a string starts with a given prefix
# or ends with a given suffix
string = input("Enter a string: ")
prefix = input("Enter a prefix to check: ")
suffix = input("Enter a suffix to check: ")
starts_with_prefix = False
ends_with_suffix = False
if string[:len(prefix)] == prefix:
    starts_with_prefix = True
if string[-len(suffix):] == suffix:
    ends_with_suffix = True
if starts_with_prefix:
    print(f"The string '{string}' starts with the prefix '{prefix}'.")
else:
    print(f"The string '{string}' does not start with the prefix '{prefix}'.")

if ends_with_suffix:
    print(f"The string '{string}' ends with the suffix '{suffix}'.")
else:
    print(f"The string '{string}' does not end with the suffix '{suffix}'.")
