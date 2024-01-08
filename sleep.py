# Create a countdown timer where the user inputs the number of seconds to 
# count down from. Use a `for` loop and `range()` to count down to zero. 
# After the loop completes, print `"Time's up!"`. You can use the `sleep()` 
# function from the `time` module to pause each iteration for one second. 
# (You can ignore any additional time needed for the loop to print out a
# number during each iteration.)
import time
time_to_sleep = input("How many seconds should I sleep: ")
time_to_sleep = int(time_to_sleep)
for second in range(time_to_sleep):
    print(second)
    time.sleep(second)
print("Time's up.")