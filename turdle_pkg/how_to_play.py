from art import tprint
from termcolor import colored

def how_to_play_turdle():
    example = colored("a", "blue", "on_yellow") + "|" + colored("m", "blue", "on_red") + "|" + colored("p", "blue", "on_yellow") + "|" + colored("l", "blue", "on_yellow") + "|" + colored("e", "blue", "on_green")
    legend1 = colored(" ", "blue", "on_green") + " = correct letter and location"
    legend2 = colored(" ", "blue", "on_yellow") + " = correct letter, wrong location"
    legend3 = colored(" ", "blue", "on_red") + " = letter does not exist in secret word"
    tprint("How to Play:", font="tarty2")
    print(f"""
    -------------------------------------------------------------------------------------------------------------
    Your objective is to guess the secret 5-letter word.

    If your guess is incorrect you will receive clues to help you with your next guess.

    Example Guess: ample

    Secret Word: plate

    Example Output:     {example}
    
    {legend1}
    {legend2}
    {legend3}
    -------------------------------------------------------------------------------------------------------------
                """)

    input("Press any key to continue...")