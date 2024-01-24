# Write a program that prints out a number ladder. Ask the user for the 
# number of steps in the ladder, and for each step, print out the step 
# number followed by the same number of asterisks
ladder = input("How many steps in the ladder? ")
ladder = int(ladder)
for step in range(ladder):
    print(f"{step + 1} {'*' * (step + 1)}")