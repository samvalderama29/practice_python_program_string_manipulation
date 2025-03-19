# Prog09: Create a program that ask the user to input their fullname in incorrect casing.
#         Print the input in pascal case.

# Display message to indicate the purpose of the program
print("Full name in pascal case")

# Prompt the user to enter their full name
fullname = input("Enter your full name: ")

# Convert the input to pascal case:
# .title() capitalizes the first letter of each word
# .split() separates the words into a list
method_name = fullname.title().split()

# Initialize an empty string to store the pascal case name
pascal_name = ""

# Loop through each word in the list and concatenate it to pascal_name
for word in method_name:
    pascal_name += word # Adds each capitalized word without spaces

# print the final pascal case formatted name
print(pascal_name)