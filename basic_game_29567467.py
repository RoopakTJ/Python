# Single-player/Multi-player Combat "Survival of the Fittest - Basic Version 1.0"
# Author: Roopak Thiyyathuparambil Jayachandran
# StudentId : 29567467
import random
import common_functions_29567467 as cf
upgrade = 0

# Welcome note
print("------------------------------------------------------------------------")
print("****** Welcome to Ultimate Combat - Survival of the fittest ************")
print("                        Basic Version - V 1                     ")
print("------------------------------------------------------------------------")


# fighter_insertion function is called multiple times to recruit the fighter for each army and fill it.
# The function in turn calls insert function which maps fighter to the digit entered
# Arguments: None
# Return: The populated army list
def fighter_insertion():
    count = 10
    player_list = []
    while count > 0:
        fighter = input()
        # checks if user-input is a digit
        if not(fighter.isdigit()):
            print("Please enter a digit from 0, 1, 2 and 3")
            continue
        else:
            fighter = int(fighter)
        # Checks if the digit equals 0,1,2 or 3
        if fighter != 1 and fighter != 2 and fighter != 3 and fighter != 0:
            print("Please enter a digit from 0, 1, 2 and 3")
            continue
        elif fighter == 0:
            break
        else:
            # In case of valid input, reduces count, calls the insert function and gives notification about the pending
            # chances to purchase
            count = count - 1
            player_list = cf.insert(fighter, player_list)
            print("Your team as of now", player_list)
            cf.fighter_count_notification(count)
    return player_list


# game_play function is called to run the battle, i.e it will check the two list values simultaneously and will pop out
# the dead fighter from the corresponding army. This function will also display the winner at the end of the battle
# Arguments: list1 - Player1 army list and list2 - Player2 army list
# Return: none
def game_play(list1=[], list2=[]):
    # Iterates through both the list and compares the first element of each list
    while len(list1) != 0 and len(list2) != 0:
        battle = cf.one_on_one_battle(list1[0], list2[0])
        # Checks the return value from the function - 0 is tie, 1 - fighter1 won, 2 - fighter2 won
        if battle == 0:
            print("both {} eliminated".format(list1[0]))
            # delete the first element from both the list
            del list1[0]
            del list2[0]

        elif battle == 1:
            print("{} died from Player2".format(list2[0]))
            # delete first element from player 2
            del list2[0]

        else:
            print("{} died from Player1".format(list1[0]))
            # delete first element from player 1
            del list1[0]
        print("fighters still on field {} from Player1 and {} from Player2".format(list1, list2))
        print("-------------------------------------------------------------------")
        # Each time function is called, the length of both the list is checked to get a winner
    if len(list1) == 0 and len(list2) == 0:
        print("-------------------------------------------------------------------")
        print(">>>>>>> The battle was a tie <<<<<<<<<<<")
        print("-------------------------------------------------------------------")

    elif len(list1) > 0:
        print("-------------------------------------------------------------------")
        print(" >>>>>>> Player 1 won the battle with {} standing strong <<<<<<<<".format(list1))
        print("-------------------------------------------------------------------")
    elif len(list2) > 0:
        print("-------------------------------------------------------------------")
        print(" >>>>>>> Player 2 won the battle with {} standing strong <<<<<<<<".format(list2))
        print("-------------------------------------------------------------------")


# player_initialization function is called for Multi-player game format in which each fighter is purchased with an
# over-all budget of 10$ for each Player
# Arguments : No arguments are passed
# Return : No return value
def player_initialization():
    print()
    print("--------------------------------------")
    print("Player 1 choose your army")
    cf.player_selection_menu(upgrade)
    player1 = fighter_insertion()
    print("Player 1 team is ready", player1)

    print()
    print("--------------------------------------")
    print("Player 2 choose your army")
    cf.player_selection_menu(upgrade)
    player2 = fighter_insertion()

    print()
    print("Player 2 team is ready", player2)
    cf.team_length_check(len(player1), len(player2))

    print()
    print("Battle begins in 3 2 1..")

    game_play(player1, player2)


# create_random_army function is called when the user selects "Single Player option"
# Random function is used to populate the bot army which will represent Player-2
# Arguments: None
# Returns: None
def create_random_army():
    print("Choose your army - Player1")
    # Player 1 army is created as usual
    cf.player_selection_menu(upgrade)
    player1 = fighter_insertion()
    player_bot = []

    # Player 2 army is auto-generated using random function. The length of the army is also auto-generated
    count = random.randrange(10) # selects from a range of 10
    item = ["Soldier", "Knight", "Archer"]

    # while loop to select the army from the list
    while count > 0:
        player_bot.append(random.choice(item))
        count = count - 1

    print("Your opponent bot army Player2 {}".format(player_bot))
    cf.team_length_check(len(player1), len(player_bot))
    print()
    print("Battle begins in 3 2 1..")

    game_play(player1, player_bot)


# single_player_multi_player function is a part of menu in which u have an option between single player or multi player
# battle
def single_player_multi_player():
    print("Menu:")

    # Single player or multi player selection. Will continue the loop until it receives a valid input
    while 1 == 1:
        selection = input("Game mode option press \n 1 - Multi player \n 2 - Single player  ")
        if selection == "1":
            # Both the army needs to be generated from user
            player_initialization()
            break
        elif selection == "2":
            # Only Player 1 army needs user input. Army 2 will be auto-generated
            create_random_army()
            break
        else:
            continue


# Game execution starts here
single_player_multi_player()

