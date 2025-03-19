# Prog07: Create a program that ask the user to input a complete statement.
#         Print the number of words in the input.

# Display message to indicate the purpose of the program
print("Count the number of words in a statement")

# Prompt the user to enter a statement
count_statement = input("Input a statement: ")

# Use split() to break the statement into a list of words
count_total = count_statement.split()

# Use len() to count the number of words in the list and print the result
print(len(count_total))