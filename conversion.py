""" import random
# Allow the user to choose whether they want to convert from feet to metres or the other way round.
# Allow the user can enter the value in the "from" unit. Make sure to include a prompt for the user!
from_unit = ""
to_unit = ""
to_value = 0
from_value = 0
test_mode = False
while not (from_unit == "feet" or from_unit == "meters"):
    from_unit = input("Do you want to convert from feet to meters, or the other way round? Enter the from unit as feet or meters: ")
    from_unit = from_unit.lower()
    test_mode = input("Test mode? True or False ")
    if test_mode == True:
        from_value = random.uniform(0.01, 1000.00)
        print(f"{from_value} converts to {from_value * 0.3048} meters and {from_value * 3.2808} feet")


# The program should also have a "test mode" which you can turn on. This test mode skips the user input. 
# Instead, it generates a random number and converts this number instead of a user input. 
 """


import sys
import random
from_unit = ""
to_unit = ""
to_value = 0
from_value = 0

TEST_MODE = False

if TEST_MODE:
    print("Running in test mode")
    from_value = random.uniform(0.01, 1000.00)
    print(f"{from_value} converts to {from_value * 0.3048} meters and {from_value * 3.2808} feet")
    TEST_MODE = False
else:
    print("Running in user input mode")
    while not (from_unit == "feet" or from_unit == "meters"):
        from_unit = input("Do you want to convert from feet to meters, or the other way round? Enter the from unit as feet or meters: ")
        from_unit = from_unit.lower()
    from_value = input(f"Enter the value in {from_unit}: ")
    # Convert to float
    from_value = float(from_value)

    # The program should then output the converted unit. Include this in a friendly phrase, using f-strings in your output!
    if from_unit == "feet":
        to_unit = "meters"
        conversion = from_value * 0.3048
    elif from_unit == "meters":
        to_unit = "feet"
        conversion = from_value * 3.2808
    print(f"{from_value} {from_unit} is {conversion} {to_unit}")
