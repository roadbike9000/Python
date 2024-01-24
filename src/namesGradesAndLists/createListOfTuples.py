# Write a program that creates a list of tuples or a list of lists with
# pairs of items, like the list used in Exercise one. Each pair of items
# consists of a name and a score between 0 and 100. You can use `random.choice()`
# to choose random names from the `list_of_names` list you used in The Baby Name
# Project
import random
grade_list = []
max_score = 99
number_of_names = random.randint(10, 100)
list_of_names = ['Amelia', 'Olivia', 'Emily', 'Alexey', 'Poppy', 'Ava', 'Isabella', 'Jessica', 'Marcus', 'Lily', 'Sophie', 'Grace', 'Vsevolod', 'Sophia', 'Mia', 'Evie', 'Ruby', 'Celim', 'Sumir', 'Ella', 'Scarlett', 'Ruben', 'Isabelle', 'Chloe', 'Cherlin', 'Sienna', 'Masha', 'Freya', 'Phoebe', 'Charlotte', 'Daisy', 'Alice', 'Florence', 'Eva', 'Sofia', 'Millie', 'Lucy', 'Evelyn', 'Elsie', 'Rosie', 'Imogen', 'Lola', 'Matilda', 'Elizabeth', 'Layla', 'Alasdair','Holly', 'Lilly', 'Molly', 'Erin', 'Ellie', 'Maisie', 'Maya', 'Abigail', 'Eliza', 'Georgia', 'Jasmine', 'Esme', 'Willow', 'Leanne', 'Bella', 'Annabelle', 'Keemiya', 'Ivy', 'Amber', 'Emilia', 'Emma', 'Summer', 'Hannah', 'Eleanor', 'Harriet', 'Rose', 'Amelie', 'Lexi', 'Megan', 'Gracie', 'Zara', 'Nuha', 'John', 'Lacey', 'Martha', 'Anna', 'Violet', 'Darcey', 'Maria', 'Maryam', 'Brooke', 'Aisha', 'Katie', 'Leah', 'Heinrich', 'Nour', 'Thea', 'Darcie', 'Hollie', 'Amy', 'Alexandra', 'Stephen', 'Jonathan', 'Penny', 'Mollie', 'Heidi', 'Lottie', 'Bethany', 'Francesca', 'Faith', 'Harper', 'Nancy', 'Beatrice', 'Isabel', 'Juliette', 'Darcy', 'Lydia', 'Sarah', 'Sara', 'Julia', 'Victoria', 'Zoe', 'Robyn', 'Oliver', 'Jack', 'Harry', 'Jacob', 'Charlie', 'Thomas', 'Annabel', 'George', 'Oscar', 'James', 'Ian', 'William', 'Noah', 'Alfie', 'Joshua', 'Yuvraj', 'Muhammad', 'Leo', 'Archie', 'Ethan', 'Joseph', 'Arushi', 'Freddie', 'Samuel', 'Alexander', 'Logan', 'Daniel', 'Isaac', 'Max', 'Mohammed', 'Benjamin', 'Hugo', 'Mason', 'Lucas', 'Edward', 'Harrison', 'Jake', 'Neil', 'Dylan', 'Asher', 'Riley', 'Akash', 'Finley', 'Catherine', 'Theo', 'Muktarsi', 'Sebastian', 'Adam', 'Zachary', 'Arthur', 'Thomas', 'Alberto', 'Toby', 'Jayden', 'Luke', 'Harley', 'Lewis', 'Tyler', 'Harvey', 'Anusha', 'Matthew', 'David', 'Reuben', 'Alok', 'Michael', 'Elijah', 'Kian', 'Tom', 'Mohammad', 'Blake', 'Jean', 'Luca', 'Theodore', 'Stanley', 'Derin', 'Jenson', 'Nathan', 'Nicholas', 'Charles', 'Frankie', 'Constantin', 'Jude', 'Teddy', 'Eric', 'Viren', 'Louie', 'Louis', 'Ryan', 'Hugo', 'Bobby', 'Niamh', 'Anya', 'Elliott', 'Dexter', 'Khai', 'Hariesh', 'Henry', 'Ollie', 'Aron', 'Alex', 'Liam', 'Kai', 'Gabriel', 'Connor', 'Aaron', 'Afrah', 'Frederick', 'Callum', 'Lorcan', 'Elliot', 'Albert', 'Leon', 'Ronnie', 'Rory', 'Jamie', 'Austin', 'Seth', 'Ibrahim', 'Mei', 'Owen', 'Caleb', 'Yousuf', 'Ellis', 'Sonny', 'Devyn', 'Robert', 'Joey', 'Felix', 'Finlay', 'Rossa', 'Ekraj', 'Jackson', 'Jimi', 'Meera', 'Rafi', 'Salahdeen', 'Guido', 'Tanya', 'Karlis']
# for i in range(10):
#     grade_list.append((random.choice(list_of_names), random.randint(50, 100)))
# print(f"The list is {grade_list}")
# print(f"The last item in the list: {grade_list[-1]}")
# print(f"The last name in the list: {grade_list[-1][0]}")

# Convert the code into a function called `generate_data()`. The function
# should take two arguments: the first is the number of items to create and
# the second is the source of names to choose from. For example,
# `generate_data(50, list_of_names)` should choose names from a list called
# `list_of_names` and create `50` name-score pairs in the list returned by the
# function.


def generate_data(number_of_items_in_the_list, source_of_names):
    grade_list = []
    for i in range(number_of_items_in_the_list):
        grade_list.append((random.choice(list_of_names), random.randint(50, 100)))
    return grade_list


# Create a second function that also has a third parameter called
# `max_score`. Use this parameter to set the maximum score of the test.
def generate_data_with_max_score(number_of_items_in_the_list, source_of_names, max_score):
    grade_list = []
    for i in range(number_of_items_in_the_list):
        grade_list.append((random.choice(list_of_names), random.randint(50, max_score)))
    return grade_list


grade_list = generate_data(number_of_names, list_of_names)
print(f"The list is {grade_list}")
print(f"The last item in the list: {grade_list[-1]}")
print(f"The last name in the list: {grade_list[-1][0]}")

grade_list = generate_data_with_max_score(number_of_names, list_of_names, max_score)
print(f"The list is {grade_list}")
print(f"The last item in the list: {grade_list[-1]}")
print(f"The last name in the list: {grade_list[-1][0]}")