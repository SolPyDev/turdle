from art import tprint
from turdle_pkg import secret, menu, highscore
from random import randint

def one_player():
    print("\nEntering One Player Game...")

    # Begins a one player game
    tprint("New Game", font="tarty2")
    secret_word = secret.secret_words[randint(0, len(secret.secret_words)-1)]
    #print(secret_word, "FOR DEBUG ONLY")
    num_guesses = 0
    while True:
        while True:
            guess = input("\nEnter a 5 letter word: ")
            if len(guess) != 5:
                print("\nYour guess MUST be 5 letters long. Try again.")
            else:
                break
        num_guesses += 1
        if guess == secret_word:
            tprint("You Win!")
            print(f"The secret word was \'{secret_word}\'")
            print(f"It took you {num_guesses} guesses to find the secret word...")
            #Ask player to record highscore
            record_high_score = input("\nWould you like to record your high score? (y/n)")
            if record_high_score == "y":
                name = input("What is your name? ")
                highscore.add_highscore(name, num_guesses, secret_word)
            #Ask player to play another game
            play_again = input("\nPlay again? (y/n) ")
            if play_again == "y":
                menu.new_game()
            else:
                menu.main_menu()
        elif guess != secret_word:
            secret.check_guess(guess, secret_word, num_guesses)

def two_player():
    print("\nEntering Two Player Game...")
    games = menu.how_many_games()
    games_counter = 0
    player_one_total = 0
    player_two_total = 0

    # Creates a two player game
    while games_counter < games:
        #Player One Turn
        tprint("Player One, Your Turn...", font="tarty2")
        secret_word = secret.secret_words[randint(0, len(secret.secret_words)-1)]
        print(secret_word, "FOR DEBUG ONLY")
        num_guesses = 0
        while True:
            while True:
                guess = input("\nEnter a 5 letter word: ")
                if len(guess) != 5:
                    print("\nYour guess MUST be 5 letters long. Try again.")
                else:
                    break
            num_guesses += 1
            if guess == secret_word:
                tprint("Congrats, you guessed the secret word!", font="tarty2")
                print(f"The secret word was \'{secret_word}\'")
                print(f"It took you {num_guesses} guesses to find the secret word...")
                player_one_total += num_guesses
                break
            else:
                secret.check_guess(guess, secret_word, num_guesses)

        #Player Two Turn
        tprint("Player Two, Your Turn...", font="tarty2")
        secret_word = secret.secret_words[randint(0, len(secret.secret_words)-1)]
        print(secret_word, "FOR DEBUG ONLY")
        num_guesses = 0
        while True:
            while True:
                guess = input("\nEnter a 5 letter word: ")
                if len(guess) != 5:
                    print("\nYour guess MUST be 5 letters long. Try again.")
                else:
                    break
            num_guesses += 1
            if guess == secret_word:
                tprint("Congrats, you guessed the secret word!", font="tarty2")
                print(f"The secret word was \'{secret_word}\'")
                print(f"It took you {num_guesses} guesses to find the secret word...")
                player_two_total += num_guesses
                break
            else:
                secret.check_guess(guess, secret_word, num_guesses)
            
        games_counter += 1
    if player_one_total < player_two_total:
        tprint("Player One Wins!")
        print("SCORE")
        print("Player One:", player_one_total, "total guesses")
        print("Player Two:", player_two_total, "total guesses")
    elif player_one_total > player_two_total:
        tprint("Player Two Wins!")
        print("SCORE")
        print("Player One:", player_one_total, "total guesses")
        print("Player Two:", player_two_total, "total guesses")
    else:
        tprint("It's a Tie!")
        print("SCORE")
        print("Player One:", player_one_total, "total guesses")
        print("Player Two:", player_two_total, "total guesses")

    play_again = input("\nPlay again? (y/n) ")
    if play_again == "y":
        two_player()
    else:
        menu.main_menu()