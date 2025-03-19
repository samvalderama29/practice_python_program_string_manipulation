# Prog06: Create a program that ask the user to input their fullname in incorrect casing.
#         Print each character of the input in reverse casing.

# Display message to indicate the purpose of the program
print("Fullname in reverse casing")

# Prompt the user to enter their full name with mixed casing
# Example input: "aNgeL" should be converted to "AnGEL"
fullname = input("Enter your full name in incorrect casing (Ex: aNgeL): ")

# Use swapcase() to reverse the casing of each letter and print the result
print(fullname.swapcase())
