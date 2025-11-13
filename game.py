# Simple text-based adventure game (starter code)

# TODO: Refactor this into a Player class
player_name = input("Enter your name, adventurer: ")
print(f"Welcome, {player_name}! Your journey begins...")

# TODO: Add an inventory system
# Example: player_inventory = []

# TODO: Add a health/points system to track player progress
# Example: player_health = 100, player_score = 0

def explore():
    print("You walk into a dark forest.")
    print("A wild creature appears!")
    action = input("Do you [fight] or [run]? ")
    if action.lower() == "fight":
        print("You bravely fight and win!")
        # TODO: Award points or add loot to inventory
        # TODO: Decrease health if the player takes damage
    elif action.lower() == "run":
        print("You escape safely, but miss out on treasure.")
        # TODO: Maybe reduce score for running away
    else:
        print("You hesitate and the creature vanishes.")
        # TODO: Add more consequences for indecision

# TODO: Add more locations (e.g., cave, village, castle) with unique events
# TODO: Create a function for random encounters (monsters, treasures, allies)

def main():
    print("Type 'explore' to begin your adventure, or 'quit' to exit.")
    # TODO: Add a 'status' command to show health, inventory, and score
    while True:
        command = input("> ")
        if command.lower() == "explore":
            explore()
        elif command.lower() == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command. Try again.")
            # TODO: Suggest valid commands when input is invalid

if __name__ == "__main__":
    main()
