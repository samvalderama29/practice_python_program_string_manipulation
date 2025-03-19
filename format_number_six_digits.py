# Prog02: Create a program that ask the user to input a number (0-1000).
#         Print the number in 6 digit format.
#         Add zeros at the beginning to complete the 6 digit.

# Display message to indicate the purpose of the program
print("Number with 6 digit beginning at 0")

# Prompt the user to enter a number from 0 - 1000
user_num_input = input("Enter a number (0 - 1000): ")

# Use zfill(6) to ensure the number is displayed with a total of 6 digits, filling with leading zeros if necessary
print(user_num_input.zfill(6))