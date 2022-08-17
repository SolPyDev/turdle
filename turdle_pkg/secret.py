from termcolor import colored

secret_words = ("adult", "agent", "anger", "apple", "award", "basis", "beach", "birth", "block", "brain", "bread", "break", "brown", "buyer", "cause", "chair", "chest", "child", "claim", "clock", "court", "coast", "cycle", "draft", "drama", "dream", "drink", "earth", "entry", "faith", "field", "floor", "force", "final", "fruit", "glass", "green", "heart", "horse", "hotel", "index", "judge", "knife", "level", "limit", "lunch", "major", "month", "noise", "novel", "nurse", "order", "other", "paper", "pilot", "pound", "press", "price", "radio", "reply", "rugby", "scene", "share", "sheet", "space", "staff", "start", "stone", "stuff", "table", "taste", "total", "trial", "uncle", "unity", "value", "video", "voice", "waste", "watch", "whole", "world" )

def check_guess(guess, secret_word, num_guesses):
    legend = colored(" ", "blue", "on_green") + " = correct letter and location\n" + colored(" ", "blue", "on_yellow") + " = correct letter, wrong location\n" + colored(" ", "blue", "on_red") + " = letter does not exist in secret word"
    text = "|"
    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            text += colored(guess[i], "blue", "on_green") + "|"
        elif guess[i] in secret_word:
            text += colored(guess[i], "blue", "on_yellow") + "|"
        else:
            text += colored(guess[i], "blue", "on_red") + "|"
    
    print("\n" + legend)
    print("\nOutput: ", text)
    print("\nGuesses so far:", num_guesses)