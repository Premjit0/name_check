# List of names
names = ["Alice", "Bob", "Charlie", "David"]

# Prompt the user to enter a name (in any case) and remove any leading or trailing whitespace.
user_input = input("Enter a name to search: ").strip()

# Check if the user_input matches any name in the list, case-insensitively.
found = False
for name in names:
    if name.lower() == user_input.lower():
        found = True
        break

# Print the result.
if found:
    print("Name found!")
else:
    print("Name not found!")
