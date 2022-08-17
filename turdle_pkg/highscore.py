import json
from art import tprint

def show_highscore():
    hs = open("turdle_pkg/highscore.txt")
    highscore_list = json.load(hs)
    print("\n\n ----------------------------------------")
    print(" ----------------------------------------")
    tprint("     Highscore", font="tarty2")
    print(" ----------------------------------------")
    print("|     NAME   |   SCORE   |   SECRET WORD |")
    print(" ----------------------------------------")
    counter = 0
    for i in highscore_list:
        print(f"       {i['name']}   --   {i['score']}   --   {i['secret']}   ")
        counter += 1
        if counter == 10:
            break

    print("\n ----------------------------------------")
    print(" ----------------------------------------")
    hs.close()

def add_highscore(name, highscore, secret_word):
    hs = open("turdle_pkg/highscore.txt")
    highscore_list = json.load(hs)
    hs.close()
    counter = 0

    for dict in highscore_list:
        if highscore < dict["score"]:
            highscore_list.insert(counter, {"name": name, "score": highscore, "secret": secret_word})
            highscore_dump = json.dumps(highscore_list)
            with open("turdle_pkg/highscore.txt", "w") as hs_file:
                hs_file.write(highscore_dump)
            print("\nNew Highscore Added!")
            break
        counter += 1

    show_highscore()
    


    