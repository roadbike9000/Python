# Bizarre queue. There's a rather bizarre queuing system in a local shop.
# People join a queue and when there are 10 people in the queue, the people
# in the second, third, fourth, and fifth position in the queue are served
# Write a program that asks the user to type in ten names, one at a time,
# and each name is added to the queue. Use slicing to show the names of the
# people in positions 2 to 5 in the queue.

people = []
count = 0
name = ""
while count < 10:
    name = input("Enter the first name of ten people one at a time: ")
    people.append(name)
    count += 1
print(f"Now serving: {people[1:5]}")
