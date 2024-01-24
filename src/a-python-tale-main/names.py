"""
1. Get the first name in the list
2. Look at the first letter
3. If the letter is "P" then write the name in another list
4. If the letter is not "P" then don't do anything
5. Look at the next name in the list
6. Repeat steps 2 - 5 until you get to the last name in the list
7. When you reach the last name in the list, stop after checking the first letter
8. Create a function to return a list of names of a specific length
"""
# letter = "P"
# names_starting_with_the_letter = []
list_of_names = ['Amelia', 'Olivia', 'Emily', 'Alexey', 'Poppy', 'Ava', 'Isabella', 'Jessica', 'Marcus', 'Lily', 'Sophie', 'Grace', 'Vsevolod', 'Sophia', 'Mia', 'Evie', 'Ruby', 'Celim', 'Sumir', 'Ella', 'Scarlett', 'Ruben', 'Isabelle', 'Chloe', 'Cherlin', 'Sienna', 'Masha', 'Freya', 'Phoebe', 'Charlotte', 'Daisy', 'Alice', 'Florence', 'Eva', 'Sofia', 'Millie', 'Lucy', 'Evelyn', 'Elsie', 'Rosie', 'Imogen', 'Lola', 'Matilda', 'Elizabeth', 'Layla', 'Alasdair','Holly', 'Lilly', 'Molly', 'Erin', 'Ellie', 'Maisie', 'Maya', 'Abigail', 'Eliza', 'Georgia', 'Jasmine', 'Esme', 'Willow', 'Leanne', 'Bella', 'Annabelle', 'Keemiya', 'Ivy', 'Amber', 'Emilia', 'Emma', 'Summer', 'Hannah', 'Eleanor', 'Harriet', 'Rose', 'Amelie', 'Lexi', 'Megan', 'Gracie', 'Zara', 'Nuha', 'John', 'Lacey', 'Martha', 'Anna', 'Violet', 'Darcey', 'Maria', 'Maryam', 'Brooke', 'Aisha', 'Katie', 'Leah', 'Heinrich', 'Nour', 'Thea', 'Darcie', 'Hollie', 'Amy', 'Alexandra', 'Stephen', 'Jonathan', 'Penny', 'Mollie', 'Heidi', 'Lottie', 'Bethany', 'Francesca', 'Faith', 'Harper', 'Nancy', 'Beatrice', 'Isabel', 'Juliette', 'Darcy', 'Lydia', 'Sarah', 'Sara', 'Julia', 'Victoria', 'Zoe', 'Robyn', 'Oliver', 'Jack', 'Harry', 'Jacob', 'Charlie', 'Thomas', 'Annabel', 'George', 'Oscar', 'James', 'Ian', 'William', 'Noah', 'Alfie', 'Joshua', 'Yuvraj', 'Muhammad', 'Leo', 'Archie', 'Ethan', 'Joseph', 'Arushi', 'Freddie', 'Samuel', 'Alexander', 'Logan', 'Daniel', 'Isaac', 'Max', 'Mohammed', 'Benjamin', 'Hugo', 'Mason', 'Lucas', 'Edward', 'Harrison', 'Jake', 'Neil', 'Dylan', 'Asher', 'Riley', 'Akash', 'Finley', 'Catherine', 'Theo', 'Muktarsi', 'Sebastian', 'Adam', 'Zachary', 'Arthur', 'Thomas', 'Alberto', 'Toby', 'Jayden', 'Luke', 'Harley', 'Lewis', 'Tyler', 'Harvey', 'Anusha', 'Matthew', 'David', 'Reuben', 'Alok', 'Michael', 'Elijah', 'Kian', 'Tom', 'Mohammad', 'Blake', 'Jean', 'Luca', 'Theodore', 'Stanley', 'Derin', 'Jenson', 'Nathan', 'Nicholas', 'Charles', 'Frankie', 'Constantin', 'Jude', 'Teddy', 'Eric', 'Viren', 'Louie', 'Louis', 'Ryan', 'Hugo', 'Bobby', 'Niamh', 'Anya', 'Elliott', 'Dexter', 'Khai', 'Hariesh', 'Henry', 'Ollie', 'Aron', 'Alex', 'Liam', 'Kai', 'Gabriel', 'Connor', 'Aaron', 'Afrah', 'Frederick', 'Callum', 'Lorcan', 'Elliot', 'Albert', 'Leon', 'Ronnie', 'Rory', 'Jamie', 'Austin', 'Seth', 'Ibrahim', 'Mei', 'Owen', 'Caleb', 'Yousuf', 'Ellis', 'Sonny', 'Devyn', 'Robert', 'Joey', 'Felix', 'Finlay', 'Rossa', 'Ekraj', 'Jackson', 'Jimi', 'Meera', 'Rafi', 'Salahdeen', 'Guido', 'Tanya', 'Karlis']


def find_names_starting_with(letter, names):
    new_names = []
    for name in list_of_names:
        if name[0] == letter:
            new_names.append(name)

    return new_names


names_starting_with_P = find_names_starting_with("P", list_of_names)
print(names_starting_with_P)

names_starting_with_A = find_names_starting_with("A", list_of_names)
print(names_starting_with_A)


def find_names_of_length(length: int, names):
    new_names = []
    for name in list_of_names:
        if len(name) == length:
            new_names.append(name)

    return new_names


names_of_length_5 = find_names_of_length(5, list_of_names)
print(names_of_length_5)
