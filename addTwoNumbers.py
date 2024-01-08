import random
# Prompt for two numbers
first_number = input("Enter a number: ")
second_number = input("Enter another number: ")

# Convert strings to integers
first_number = int(first_number)
second_number = int(second_number)

# Sum the two numbers and print the sum
total = first_number + second_number
print(f"The sum of {first_number} and {second_number} is {total}")

# Print a random number between the two inputs
random_number = random.randint(first_number, second_number)
print(f"{random_number} is a random number between your two numbers.")
