# Keep rising. Write a program which generates random numbers between 1 and 100. 
# Your program should only keep a number if it's larger than or equal to the 
# previous number. If the number is smaller than the previous number, discard 
# the new number and generate a new one. This means your numbers should be form 
# an increasing sequence of numbers. Store the sequence of numbers in a list 
# and print it. Print out the length of your final list and how many iterations 
# it took to generate this list. Your output should look like this:
# The list of numbers is [43, 81, 89, 97, 99, 100]
# It took 145 iterations to create this list

import random
""" list_of_numbers = []
total_iterations = 0
previous_number = 0
current_number = random.randint(1, 100)
while current_number >= previous_number:
    list_of_numbers.append(current_number)
    total_iterations += 1
    previous_number = current_number
    current_number = random.randint(1, 100)
print(f"The list of numbers is {list_of_numbers}")
print(f"It took {total_iterations} iterations to create this list") """

# Extend the code so that you generate 20 lists following the same rules. 
# Show the number of iterations for each one. At the end, show the average 
# number of iterations required.
maximum_loops = 20
grand_total_iterations = 0
for i in range(maximum_loops):
    list_of_numbers = []
    total_iterations = 0
    previous_number = 0
    current_number = random.randint(1, 100)
    while current_number >= previous_number:
        list_of_numbers.append(current_number)
        total_iterations += 1
        previous_number = current_number
        current_number = random.randint(1, 100)
    print(f"The list of numbers is {list_of_numbers}")
    print(f"It took {total_iterations} iterations to create this list")
    grand_total_iterations += total_iterations

print(
    f"The average number of iterations was "
    f"{grand_total_iterations / maximum_loops} \n"
)
