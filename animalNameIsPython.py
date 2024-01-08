# Prompt for name of animal
# Check if animal name is "python"
# If yes, Print "Did you know..."
# if no, repeat the prompt to enter an animal name

guessed_animal_name = False

while not guessed_animal_name:
    animal_name = input("Enter the name of an animal: ")
    animal_name = animal_name.lower()

    if (animal_name == "python"):
        guessed_animal_name = True

print(
    "Thanks for playing. "
    "Did you know that the programming language Python wasn't "
    "named after the snake?"
)
