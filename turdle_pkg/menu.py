from art import tprint
from turdle_pkg import game, highscore, how_to_play

# Displays the main menu
def main_menu():
    while True:
        print("""
        -----------------Menu------------------
        | 1. How to Play   |  2.  New Game    |
        ---------------------------------------
        | 3. High Score    |  4.  Quit        |
        ---------------------------------------""")
        option = input("            Enter your selection: ")

        if option == "1":
            how_to_play.how_to_play_turdle()
        elif option == "2":
            new_game()
        elif option == "3":
            highscore.show_highscore()
        elif option == "4":
            quit()
        else:
            print("Invalid selection. Please try again.")

def new_game():
    while True:
        print("""
        ----------- How Many Players?----------
        | 1.  One Player   |  2.  Two Player  |
        ---------------------------------------""")
        option = input("            Enter your selection: ")

        if option == "1":
            game.one_player()
        elif option == "2":
            game.two_player()
        else:
            print("Invalid selection!")
            continue

def how_many_games():
    while True:
        print("""
        ----------- How Many Games?------------
        | 1.  One         |  2.    Two        |
        ---------------------------------------
        | 3.  Three       |  4.    Four       |
        ---------------------------------------""")
        option = int(input("            Enter your selection: "))
        if option < 1 or option > 4:
            print("\nInvalid Selection!")
            continue
        else:
            return option
