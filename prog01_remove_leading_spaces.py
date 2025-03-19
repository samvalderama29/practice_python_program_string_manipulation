# Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning.
#         Print the input without the spaces in the beginning.

# Display message to indicate the purpose of the program
print("Fullname without spaces")

# Prompt the user to enter their full name with leading spaces (Ex:     Sam)
fullname = input("Enter your full name (must have several space characters at the beginning): ")

# Remove leading spaces using the lstrip() method and print the result
print(fullname.lstrip())