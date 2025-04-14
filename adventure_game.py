import time
import random
import sys


def print_pause(message):
    """Print a message and then pause for 2 seconds."""
    print(message)
    time.sleep(2)


def valid_input(prompt, valid_options):
    """
    Keep asking the user for input until they enter one of the valid options.
    Returns the user's choice as a string.
    """
    while True:
        response = input(prompt).lower()
        if response in valid_options:
            return response
        print_pause(f"Invalid choice! Please enter one of {valid_options}.")


def ascii_sword():
    """
    A simple ASCII art sword.
    You can replace or enhance it as you wish.
    """
    print("          /|")
    print("         / |      (The magical Sword of Ogoroth)")
    print("        /  |")
    print("       /   |")
    print("      /    |")
    print("     /_____|")
    print()


def intro(enemy):
    """
    Print the introduction describing the initial setting of the game.
    """
    print_pause("You find yourself standing in an open field,")
    print_pause("filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a wicked {enemy} is lurking around,")
    print_pause("terrorizing the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand, you hold your trusty (but not very effective)")
    print_pause("dagger.")


def cave(items):
    """
    Scenario when the player chooses to explore the cave.
    If the player doesn't have the sword, they will find it here.
    Otherwise, there's nothing new.
    """
    print_pause("You peer cautiously into the cave...")
    if "sword" in items:
        print_pause("You've already picked up the magical sword.")
        print_pause("There is nothing else to find here.")
    else:
        print_pause("It turns out to be a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        ascii_sword()
        print_pause("You discard your silly old dagger and take the sword.")
        items.append("sword")
    print_pause("You walk back out to the field.")


def fight(items, enemy):
    """
    Scenario where the player engages in a fight with the enemy.
    If they have the sword, they win. Otherwise, they lose.
    """
    if "sword" in items:
        print_pause(f"As the {enemy} moves to attack, you unsheathe your new "
                    "sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand.")
        print_pause(f"In a blazing strike, you defeat the {enemy}!")
        print_pause("You have saved the town. You are victorious!")
    else:
        print_pause("You do your best with your tiny dagger,")
        print_pause(f"but the {enemy} overpowers you!")
        print_pause("You have been defeated!")

    play_again()


def house(items, enemy):
    """
    Scenario when the player enters the house.
    Depending on the items, the player will feel ready or not.
    """
    print_pause("You approach the door of the house...")
    print_pause("It creaks open, and you step inside.")
    print_pause("Suddenly, the door slams shut behind you!")
    if "sword" in items:
        print_pause(f"You're ready to fight the {enemy} with your new sword!")
    else:
        print_pause("You feel a bit under-prepared for this,")
        print_pause("only having a tiny dagger.")

    choice = valid_input("Would you like to (1) fight or (2) run away?\n",
                         ["1", "2"])
    if choice == "1":
        fight(items, enemy)
    else:
        print_pause("You run back into the field. Luckily, you don't seem to")
        print_pause("have been followed.")
        field(items, enemy)


def field(items, enemy):
    """
    Main field scenario, where the player chooses their next action:
    1) Enter the house
    2) Explore the cave
    3) Exit the game
    """
    print_pause("\nYou find yourself back in the peaceful field.")
    print_pause("What would you like to do?")
    choice = valid_input("Enter 1 to knock on the door of the house.\n"
                         "Enter 2 to peer into the cave.\n"
                         "Enter 3 to exit the game.\n"
                         "(Please enter 1, 2, or 3.)\n",
                         ["1", "2", "3"])
    if choice == "1":
        house(items, enemy)
    elif choice == "2":
        cave(items)
        field(items, enemy)
    else:
        print_pause("Thank you for playing! Goodbye.")
        sys.exit(0)


def play_game(enemies_list):
    """
    Main function to start a new round of the game:
    - If enemies_list is empty, refill it with the original enemies.
    - Randomly choose an enemy, remove it from the list.
    - Reset the player's items.
    - Show the intro, then go to the field scenario.
    """
    if not enemies_list:
        enemies_list.extend(["pirate", "troll", "wicked fairie",
                             "dragon", "gorgon"])

    enemy = random.choice(enemies_list)
    enemies_list.remove(enemy)

    items = []

    intro(enemy)
    print_pause("You head back to the field.")
    field(items, enemy)


def play_again():
    """
    After winning or losing a fight, ask the player
    if they want to play again.
    """
    again = valid_input("Would you like to play again? (y/n)\n", ["y", "n"])
    if again == "y":
        print_pause("Excellent! Restarting the game...\n")
        play_game(ENEMIES)
    else:
        print_pause("Thanks for playing! See you next time.")
        sys.exit(0)


ENEMIES = ["pirate", "troll", "wicked fairie", "dragon", "gorgon"]


def main():
    """
    Entry point of the application.
    """
    print_pause("Welcome to the Text-Based Adventure Game!")
    play_game(ENEMIES)


if __name__ == "__main__":
    main()
