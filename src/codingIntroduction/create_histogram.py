# Prompt the user to enter several integers within a single line, separated by spaces. 
# Your program should then display a horizontal histogram for each number, 
# using a sequence of asterisks. For example, if the user inputs `4 7 2`, the output should be:

"""
****
*******
**
"""
# numbers_of_stars = input("Enter a list of numbers separated by spaces: ")


def create_histogram(input_string):
    list_of_numbers = input_string.split()
    output = []
    if not list_of_numbers:
        output = ["No input provided. Please enter a list of integers separated by spaces.\n"]
    else:
        try:
            for number in list_of_numbers:
                integer_value = int(number)
                output.append("*" * integer_value)
        except ValueError:
            output = ["Sorry, some of the values are not integers. Please enter integers separated by spaces.\n"]
    return output


if __name__ == "__main__":
    numbers_of_stars = input("Enter a list of numbers separated by spaces: ")
    print(*create_histogram(numbers_of_stars), sep='\n')
