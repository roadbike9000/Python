import random

# Assign a random number to two die
""" die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

# Print the values of the two die
print(die1, die2) """

# Keep rolling until doubles
# Print all pairs on separate lines
# Display special message for double sixes

doubles_thrown = False
special_roll = 6

while not doubles_thrown:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    print(die1, die2)
    if (die1 == die2):
        print("Congratulations, you rolled a double.")
        doubles_thrown = True
        if (die1 == special_roll):
            print("Congratulations, you rolled a magic double!")
