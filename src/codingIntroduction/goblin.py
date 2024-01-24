
import random

number_of_doors = 10  # Create welcome messages
print("Welcome to the Game")
player_name = input("Type your name: ")
print(f"Hello {player_name}! JefLet's play.")

# Display the doors
print("|_|" * number_of_doors)

# Set the location of the goblin
goblin_position = random.randint(1, number_of_doors)

# Logic for the game
game_running = True
while game_running:
    player_guess = input(
        f"Which door is the goblin hiding behind? "
        f"[1 - {number_of_doors}]: "
    )
    player_guess = int(player_guess)

    # If the player guesses correctly, congratulate then exit the game
    # else continue the game
    if player_guess == goblin_position:
        print("Well done!")
        game_running = False
    else:
        print("No, the goblin is not there. Please try again.")

print("Game over!")
