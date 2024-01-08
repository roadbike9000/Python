# Ask the user for an odd-numbered height and produce a diamond pattern of the 
# given height. For example, if the user enters `5`, the diamond will look like
"""
  *
 ***
*****
 ***
  *
"""

height = 0
# Prompt for an odd number
while (height % 2 == 0):
    height = input("Enter an odd number: ")
    height = int(height)
for i in range(height + 1):
    if i % 2 == 1:
        print(f"{'*' * i}".center(height))
for i in range(height - 1, -1, -1):
    if i % 2 == 1:
        print(f"{'*' * i}".center(height))