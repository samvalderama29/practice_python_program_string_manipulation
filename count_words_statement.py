# Prog07: Create a program that ask the user to input a complete statement.
#         Print the number of words in the input.

print("Count the number of words in a statement")

count_statement = input("Input a statement: ")

count_total = count_statement.split()

print(len(count_total))