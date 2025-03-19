# Prog02: Create a program that ask the user to input a number (0-1000).
#         Print the number in 6 digit format.
#         Add zeros at the beginning to complete the 6 digit.

print("Number with 6 digit beginning at 0")

user_num_input = input("Enter a number (0 - 1000): ")

print(user_num_input.zfill(6))