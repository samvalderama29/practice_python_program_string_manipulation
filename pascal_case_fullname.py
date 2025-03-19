# Prog09: Create a program that ask the user to input their fullname in incorrect casing.
#         Print the input in pascal case.

print("Full name in pascal case")

fullname = input("Enter your full name: ")

method_name = fullname.title().split()

pascal_name = ""

for word in method_name:
    pascal_name += word

print(pascal_name)