# Single-player/Multi-player Combat "Survival of the Smartest - Extended Version 2.0"
# Author: Roopak Thiyyathuparambil Jayachandran
# StudentId : 29567467

import random
import common_functions_29567467 as cf

# Welcome note
print("----------------------------------------------------------------------")
print("******* Welcome to Ultimate Combat - Survival of the Smartest ********")
print("--------------------------------Version 2.0---------------------------")
player_medics = 0
player1_medics = 0
player2_medics = 0
bot_medics = 0
upgrade = 0


# fighter_insertion function is called multiple times to recruit the fighter for each army and fill it. In case of
# upgrade option, new fighters can also be added with 4 - siege equipment and 5 - wizard
# The function in turn calls insert function which maps fighter to the digit entered
# Arguments: None
# Return: The populated army list
def fighter_insertion():
    count = 10
    player_list = []
    global player_medics
    player_medics = 0
    while count > 0:
        fighter = input()
        # Checks for valid input
        if not (fighter.isdigit()):
            print("Please enter a digit from 0, 1, 2 and 3")
            continue
        else:
            fighter = int(fighter)
        if fighter == 0:
            player_medics = count
            break

        # if upgrade version is expanded army or both
        if (upgrade == 2 or upgrade == 3) and (fighter != 1 and fighter != 2 and fighter != 3 and fighter != 4 and fighter != 5 \
                and fighter != 0):
            print("Please enter a digit from 0, 1, 2, 3, 4 and 5")
            continue
        # if upgrade option selected is medics only
        elif (upgrade != 2 and upgrade != 3) and fighter != 1 and fighter != 2 and fighter != 3:
            print("Please enter a digit from 0, 1, 2, 3")
            continue
        else:
            # For upgrade expanded army or both
            if upgrade == 2 or upgrade == 3:
                # If fighter is "Siege command", check if budget is available
                if fighter == 4 and count - 2 < 0:
                    print("You don't have enough budget to buy siege. Available budget is {}".format(count))
                    continue
                # If fighter is "Wizard", check if budget is available
                if fighter == 5 and count - 3 < 0:
                    print("You don't have enough budget to buy wizard. Available budget is {}".format(count))
                    continue
                else:
                    # If fighter is "Siege Command", count has to be reduced by 2
                    if fighter == 4:
                        count = count - 2
                    # If fighter is "Wizard", count has to be reduced by 3
                    elif fighter == 5:
                        count = count - 3
                    else:
                        count = count - 1
                    player_list = cf.insert(fighter, player_list)
                    print("Your team as of now", player_list)
                    cf.fighter_count_notification(count)
            else:
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
    global player1_medics
    global player2_medics

    while len(list1) != 0 and len(list2) != 0:
        battle = cf.one_on_one_battle(list1[0], list2[0])

        # if both the fighters are same, both will be eliminated. If medics upgrade is enabled, then it will check the
        # available medics and re-enter the army accordingly
        if battle == 0:
            print("both {} eliminated".format(list1[0]))

            if (upgrade == 1 or upgrade == 3) and player1_medics > 0:
                player1_medics = player1_medics - 1
                print("Medics used : {} re-entered the army. Medics left for player 1 is {}".format(list1[0],
                                                                                                  player1_medics))
                # First element is popped and appended towards the end if medics is available
                killed_fighter1 = list1.pop(0)
                list1.append(killed_fighter1)
            if (upgrade == 1 or upgrade == 3) and player2_medics > 0:
                player2_medics = player2_medics - 1
                print("Medics used : {} re-entered the army. Medics left for player 2 is {}".format(list2[0],
                                                                                                   player2_medics))
                killed_fighter2 = list2.pop(0)
                list2.append(killed_fighter2)
            else:
                # if player_medics is not available or if upgrade is not medics
                del list1[0]
                del list2[0]

        elif battle == 1:
            print("{} died from Player2".format(list2[0]))
            if (upgrade == 1 or upgrade == 3) and player2_medics > 0:
                player2_medics = player2_medics - 1
                print("Medics used : {} re-entered the army. Medics left for player 2 is {}".format(list2[0],
                                                                                                   player2_medics))
                # First element is popped and appended towards the end if medics is available
                killed_fighter2 = list2.pop(0)
                list2.append(killed_fighter2)
            else:
                del list2[0]

        else:
            print("{} died from Player1".format(list1[0]))
            if (upgrade == 1 or upgrade == 3) and player1_medics > 0:
                player1_medics = player1_medics - 1
                print("Medics used : {} re-entered the army. Medics left for player 1 is {}".format(list1[0],
                                                                                                   player1_medics))
                # First element is popped and appended towards the end if medics is available
                killed_fighter1 = list1.pop(0)
                list1.append(killed_fighter1)
            else:
                del list1[0]

        print("fighters still on field {} from Player1 and {} from Player2".format(list1, list2))
        print("-------------------------------------------------------------------")
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
    global player1_medics
    global player2_medics
    global player_medics

    print("----------------------------------------------------------------------------------------")
    print("Player 1 choose your army")
    cf.player_selection_menu(upgrade)
    player1 = fighter_insertion()

    # in case of medics upgrade, player_medics or count is assigned to player1_medics
    if upgrade == 1 or upgrade == 3:
        player1_medics = player_medics
        print("Medics of {} available for player 1".format(player1_medics))

    print("Player 1 team is ready", player1)

    print()
    print("Player 2 choose your army")
    cf.player_selection_menu(upgrade)
    player2 = fighter_insertion()
    # in case of medics upgrade, player_medics or count is assigned to player2_medics
    if upgrade == 1 or upgrade == 3:
        player2_medics = player_medics
        print("Medics of {} available for player 2".format(player2_medics))

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

    global player1_medics
    global player2_medics

    # Player 1 army is inserted by the user
    cf.player_selection_menu(upgrade)
    player1 = fighter_insertion()
    if upgrade == 1 or upgrade == 3:
        player1_medics = player_medics
        print("Medics of {} available for player 1".format(player1_medics))

    player_bot = []
    # Player 2 army is auto-generated using random function. The length of the army is also auto-generated
    count = random.randrange(5,10)
    bot_medics = count
    if upgrade == 2 or upgrade == 3:
        item = ["Soldier", "Knight", "Archer", "Wizard", "Siege"]
    else:
        item = ["Soldier", "Knight", "Archer"]
    item2 = ["Soldier", "Knight", "Archer"]

    print("Budget used by bot army is ", count)
    while count > 0:
        if count < 3:
            player_bot.append(random.choice(item2))
        else:
            player_bot.append(random.choice(item))
        # If auto generated fighter is Siege ot Wizard, count value is calculated accordingly
        if player_bot[len(player_bot)-1] == "Siege":
            count = count - 2
        elif player_bot[len(player_bot)-1] == "Wizard":
            count = count - 3
        else:
            count = count - 1

    print("Your opponent bot army Player2 {}".format(player_bot))
    cf.team_length_check(len(player1), len(player_bot))
    if upgrade == 1 or upgrade == 3:
        player2_medics = 10 - bot_medics
        print(" Medics available for the bot army is :", player2_medics)

    print()
    print("Battle begins in 3 2 1..")

    game_play(player1, player_bot)


# single_player_multi_player function is a part of menu in which u have an option between single player or multi player
# battle
def single_player_multi_player():
    print("Menu:")

    # Single player or multi player selection. Will continue the loop until it receives valid input
    while 1 == 1:
        selection = input("Game mode option press \n 1 - Multi player \n 2 - Single player  ")
        if selection == "1":
            player_initialization()
            break
        elif selection == "2":
            create_random_army()
            break
        else:
            continue


def upgrades():
    while 1 == 1:
        u = input("\nUpgrades are available for this version of Battle. Choose your option \n 1 - Medics"
                  " \n 2 - Expanded Armies \n 3 - Choose both ")
        if u == "1" or u == "2" or u == "3":
            return int(u)
        else:
            print("Please enter a valid input")


upgrade = upgrades()
single_player_multi_player()
