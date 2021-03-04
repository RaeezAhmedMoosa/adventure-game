# This is Version 4 of the Python Adventure Game project.

# These are the imported modules for the game.
import time
import random

# This is the empty list which is used as an "inventory" for the player.
items = []

# Below are Lists containing a variety of items to be used within the game as
# randomised text.
animal = ["Rat", "Hamster", "Gecko", "Trout", "Wallaby", "Meerkat", "Toad",
          "Sloth", "Manatee", "Pigeon", "Mole", "Gerbil", "Dolphin", "Beaver"]


beast = ["Muppet", "basilisk", "Magikarp", "nightwraith", "Gary Busey",
         "werewolf", "Spanish tax collector", "ghoul", "Kardashian", "dragon"]


language = ["English", "Dothraki", "Spanish", "Nilfgaardian", "Arabic",
            "Python", "French", "Chakobsa", "Mandarin", "High Valyrian"]


weapon = ["Brightroar", "Blackfyre", "Dark Sister", "Lamentation", "Truth",
          "Vigilance", "Orphan-Maker", "Longclaw", "Heartsbane", "Nightfall"]


# This is the section for all the Functions for the game.
def print_pause(text):
    time.sleep(3)
    print(text)


# This function ensures that a new set of randomised items are chosen upon
# restarting a game.
def pre_game():
    global animal1
    global beast1
    global language1
    global weapon1
    animal1 = random.choice(animal)
    beast1 = random.choice(beast)
    language1 = random.choice(language)
    weapon1 = random.choice(weapon)


# This is function for the introduction portion of the game. Here some of the
# randomly generated words, taken from the lists at the start, are used for the
# first time.
def intro():
    print_pause("\nYou find yourself standing in an open field, filled with "
                "lush green grass and blooming yellow wildflowers.\n")
    print_pause("You are a Witcher-in-Training who has recently passed the "
                "infamous 'Trials of the Grasses'.\n")
    print_pause("You hail from the lesser-known School of "
                "the " + animal1 + ".\n")
    print_pause("Rumour has it that a " + beast1 + " is somewhere around here,"
                " and has been terrifying the nearby town.\n")
    print_pause("In front of you stands an imposing house.\n")
    print_pause("Off to your right, in the distance, is a dark cave.\n")
    print_pause("In your hand, you grasp your rusty but trusty (albeit not"
                " very effective) dagger.\n")


# This is the function that deals with any invalid input entered by the player.
def bad_input():
    print_pause("\nInvalid input, please try again.\n")


# This is the function that displays the choices that are available to the
# player during certain portions of the game.
def choice_prompt():
    print_pause("Enter 1 to fight.\n"
                "Enter 2 to run away\n")


# This function displays messages indicating to the player what type of input
# to use when prompted to do so by the game.
def input_prompt():
    print_pause("What would you like to do?\n"
                "\n(Please enter 1 or 2)\n")


# This function deals with the Field area of the game, which is basically the
# 'Landing' area of the game where the player will fall back to often while
# playing the game.
def field():
    print_pause("Enter 1 to knock on the door of the house.\n"
                "Enter 2 to travel to and search the cave.\n")
    input_prompt()
    choice = input("")
    if choice == "1":
        house()
    elif choice == "2":
        cave()
    else:
        bad_input()
        field()


# This function gives the player the choice to either exit the game or restart
# the game. If the player chooses to restart, the player's inventory from their
# initial playthrough is 'emptied' in order to start the game anew.
def restart():
    print_pause("GAME OVER\n")
    while True:
        print_pause("Would you like to play again? (y/n)\n")
        choice = input("")
        if choice == "y":
            if "sword" in items:
                items.remove("sword")  # This line empties the 'inventory'
            start_game()
            break
        elif choice == "n":
            print_pause("\nThank you for playing. Goodbye!")
            break
        else:
            bad_input()


# This functions deals with the player choosing to run away in certain areas,
# with the player returning to the 'Field' area each time.
def run_away():
    print_pause("\nJust like a " + animal1.lower() + ", you dash off in the "
                "opposite direction back to the field with the lush green "
                "grass.\n")
    print_pause("Fortunately, you don't seem to have been followed by the "
                + beast1 + " in your hasty retreat.\n")
    field()


# This function deals with the Fight between the player and the beast, if the
# player obtained the sword, they will win the game.
def fight_win():
    print_pause("\nAs the " + beast1 + " lunges towards you, "
                "you draw " + weapon1 + ".\n")
    print_pause(weapon1 + "'s Valyrian steel shines brightly in your hands as "
                "you brace yourself for the attack.\n")
    print_pause("*Panics in " + language1 + "*\nThe " + beast1 + " takes a "
                "fearful glance at " + weapon1 + " and decides to flee!\n")
    print_pause("You have rid the town of the evil " + beast1 + ". You are "
                "victorious!\n")
    print_pause("*Townfolks cheer in " + language1 + "!*\n")
    print_pause("WINNER IS YOU!!!")
    restart()


# This function deals with the Fight between the player and the beast, if the
# player did not obtain the sword & chooses to fight, the player will lose.
def fight_lose():
    print_pause("\nYou do your best...\n"
                "...but your dagger (and general inexperience) is no match for"
                " the " + beast1 + ".\n")
    print_pause("You have been defeated!\n")
    print_pause("*Townfolks cry in " + language1 + "*\n")
    restart()


# This function deals with the 'House' section of the game. Depending on the
# player's choices, the player can either win or lose the game if the player
# elects to fight when prompted.
def house():
    print_pause("\nYou cautiously approach the door of the house.\n")
    print_pause("As you move your hand close to the door, the door opens "
                "suddenly, and out steps the " + beast1 + ".\n")
    print_pause("*Gasps in " + language1 + "!*\nThis is the " + beast1 + "'s "
                "house!\n")
    print_pause("Almost immediately, the " + beast1 + " attacks you!\n")
    while True:
        if "sword" in items:
            print_pause("With " + weapon1 + " in your possession, you almost"
                        " feel like a fully qualified Witcher...\n")
            choice_prompt()
            input_prompt()
            choice = input("")
            if choice == "1":
                fight_win()
                break
            elif choice == "2":
                run_away()
                break
            else:
                bad_input()
        else:
            print_pause("You feel a bit under-prepared for this, what with "
                        "only possessing a tiny (rusted) dagger.\n")
            choice_prompt()
            input_prompt()
            choice = input("")
            if choice == "1":
                fight_lose()
                break
            elif choice == "2":
                run_away()
                break
            else:
                bad_input()


# This function deals with the 'Cave' area. This is where the player finds the
# sword needed to win the game. There are no choices available to player here.
def cave():
    if "sword" in items:
        print_pause("\nYou have been to this cave before and found all the "
                    "good loot. It's just an empty cave now.\n")
        print_pause("You trek your way back to the field with the yellow "
                    "wildflowers.\n")
        field()
    else:
        print_pause("\nYou make your way through the wilderness towards the "
                    "cave.\n")
        print_pause("With the caution and awareness that you honed at the "
                    "School of the " + animal1 + ", you survey the cave.\n")
        print_pause("It turns out that the cave is quite small and shallow.\n")
        print_pause("Your " + animal1.lower() + "-like eyes catch a glint of "
                    "metal behind a rock.\n")
        print_pause("You move silently towards the rock to find the source of "
                    "that glint.\n")
        print_pause("'Praise Geraldo' you mutter in disbelief!\n")
        print_pause("You have found the magical sword '" + weapon1 + "'!\n")
        items.append("sword")  # Sword is added to the player's inventory.
        print_pause("You toss your silly old dagger aside and take the sword "
                    "with you.\n")
        print_pause("* 'Trusty' old dagger has been removed from your "
                    "inventory *\n")
        print_pause("* " + weapon1 + " has been added to your inventory *\n")
        print_pause("You trek your way back to the field with the yellow "
                    "wildflowers.\n")
        field()


# This is the function containing all the necessary functions for the player
# to play the game.
def start_game():
    pre_game()
    intro()
    field()


start_game()
