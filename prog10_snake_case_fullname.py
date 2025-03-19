# Prog10: Create a program that ask the user to input their fullname in incorrect casing.
#         Print the input in snake case.

# Display message to indicate the purpose of the program
print("Full name in pascal case")

# Prompt the user to enter their full name
fullname = input("Enter your full name: ")

# Convert the full name to lowercase
lowercase_name = fullname.lower()

# Replace spaces with underscores to convert to snake_case and print the result
print(lowercase_name.replace(" ", "_"))