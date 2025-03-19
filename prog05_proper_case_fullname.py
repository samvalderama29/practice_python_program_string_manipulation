# Prog05: Create a program that ask the user to input their fullname in incorrect casing.
#         Print the input in proper casing.

# Display message to indicate the purpose of the program
print("Fullname proper casing")

# Prompt the user to enter their full name with incorrect casing
# Example: User enters "aNgeL" instead of "Angel"
fullname = input("Enter your full name in incorrect casing (Ex: aNgeL): ")

# Convert the first letter of each name to uppercase and the rest to lowercase using title() method
print(fullname.title())