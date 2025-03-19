# Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning.
#         Print the input without the spaces in the beginning.

print("Fullname without spaces")

fullname = input("Enter your full name (must have several space characters at the beginning): ")

print(fullname.lstrip())