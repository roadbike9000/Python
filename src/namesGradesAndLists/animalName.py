# Prompt for name of animal
# Check if animal name is "python"
# If yes, Print "Did you know..."
# if no, print "Cool...<animal name> is a great animal"

animal_name = input("Enter the name of an animal: ")
animal_name = animal_name.lower()
if (animal_name == "python"):
    print("Did you know that the programming language Python wasn't named after the snake?")
else:
    print(f"Cool..{animal_name} is a great animal.")