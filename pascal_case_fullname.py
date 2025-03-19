# Prog09: Create a program that ask the user to input their fullname in incorrect casing.
#         Print the input in pascal case.

print("Full name in pascal case")

fullname = input("Enter your full name: ")

pascal_name = fullname.capitalize(), fullname.strip()

print(pascal_name)