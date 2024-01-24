# Prompt the user to enter several integers within a single line, separated by spaces. 
# Your program should then display a horizontal histogram for each number, 
# using a sequence of asterisks. For example, if the user inputs `4 7 2`, the output should be:

"""
****
*******
**
"""
numbers_of_stars = input("Enter a list of numbers separated by spaces: ")
list_of_numbers = numbers_of_stars.split()
for number in list_of_numbers:
    print(f"{'*' * int(number)}")
