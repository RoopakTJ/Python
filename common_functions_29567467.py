# Single-player/Multi-player Combat "Common function"
# Author: Roopak Thiyyathuparambil Jayachandran
# StudentId : 29567467
# File contains common function which are used across both the games


# insert function maps user entered digits to fighter strings and appends that to the army list.
# Arguments: the fighter digit entered by the user and list as of now
# Return: the function returns the list after the newly recruited fighter is appended to it.
def insert(fighter, list=[]):
    if fighter == 1:
        print("You bought an Archer")
        list.append("Archer")
    if fighter == 2:
        print("You bought a Soldier")
        list.append("Soldier")
    if fighter == 3:
        print("You bought a Knight")
        list.append("Knight")
    if fighter == 4:
        print("You bought a Siege Equipment")
        list.append("Siege")
    if fighter == 5:
        print("You bought a Wizard")
        list.append("Wizard")
    return list


# fighter_count_notification notifies the Player the pending budget each time a fighter is recruited
# Arguments: Count of pending fighters which was computed in a while loop of fighter_insertion function
# Return: None
def fighter_count_notification(count):
    if count == 1:
        print("Please choose your last fighter".format(count))
    elif count == 0:
        print("Your budget is over")
    else:
        print("You can buy {} more fighters".format(count))


# team_length_check function does an initial check if any/both of the army(s) is empty. In that case it will declare
# the other Player as the winner
# Argument: length of both the teams (int)
# return: will exit the battle in case length is 0.
def team_length_check(length_first, length_second):
    if length_first == 0 and length_second == 0:
        print("-------------------------------------------------------------------")
        print("Battle ends. It is a tie")
        print("-------------------------------------------------------------------")
        exit(0)
    elif length_first == 0:
        print("-------------------------------------------------------------------")
        print("Player 2 wins the battle")
        print("-------------------------------------------------------------------")
        exit(0)
    elif length_second == 0:
        print("-------------------------------------------------------------------")
        print("Player 1 wins the battle")
        print("-------------------------------------------------------------------")


# one_on_one_battle function is called to check the strength and weakness of each fighter with the other. This function
#  will also decide and print who was the winner in individual battle
# arguments: fighter1 - single fighter from one army, fighter2 - single fighter from another army
# return: 0 - both fighters are eliminated
# 1 - second fighter is eliminated
# 2 - first fighter is eliminated
def one_on_one_battle(fighter1, fighter2):
    # A list of list is initialized with each fighter, his strength list and weakness list
    # Format used ["Fighter",["Strength"],{"Weakness"}]
    # This will make the program scalable if we want to add more individual units
    strength_weakness_list_expanded = [["Archer", ["Soldier", "Wizard"], ["Knight", "Siege"]],
                                       ["Soldier", ["Knight"], ["Archer", "Wizard", "Siege"]],
                                       ["Knight", ["Archer", "Siege"], ["Soldier", "Wizard"]],
                                       ["Siege", ["Archer", "Soldier"], ["Wizard", "Knight"]],
                                       ["Wizard", ["Soldier", "Knight", "Siege"], ["Archer"]]]

    print()
    print(" > Battle is between {} and {}".format(fighter1, fighter2))

    # If both the fighters are same, return 0
    if fighter1 == fighter2:
        return 0

    for item in range(len(strength_weakness_list_expanded)):
        if strength_weakness_list_expanded[item][0] == fighter1:
            # checks if fighter 2 is present in strength list, in that case return 1
            for strength in range(len(strength_weakness_list_expanded[item][1])):
                if strength_weakness_list_expanded[item][1][strength] == fighter2:
                    return 1
            # checks if the fighter 2 is present in weakness list, in that case return 2
            for weakness in range(len(strength_weakness_list_expanded[item][2])):
                if strength_weakness_list_expanded[item][2][weakness] == fighter2:
                    return 2


# The function player_selection_menu is called to list the available purchase options for each game level.
# For the upgrade version, it will also display newly added fighter list with cost
def player_selection_menu(upgrade):

    if upgrade == 2 or upgrade == 3:
        print("Choose your option from 0,1,2,3,4,5. Warning: Siege equipment and wizard are costly")
        print("1 - Archer     -      $1")
        print("2 - Soldier    -      $1")
        print("3 - Knight     -      $1")
        print("4 - Siege Equipment - $2")
        print("5 - Wizard     -      $3")
        print("0 - Done with the selection")
    else:
        print("Choose your option from 0,1,2,3")
        print("1 - Archer     -      $1")
        print("2 - Soldier    -      $1")
        print("3 - Knight     -      $1")
        print("0 - Done with the selection")


