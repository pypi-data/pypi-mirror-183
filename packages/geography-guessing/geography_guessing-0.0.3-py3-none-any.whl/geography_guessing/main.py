import string
import random
import pandas as pd


def game():
    df = pd.read_csv('country-list.csv')
    scores = pd.read_csv("gamesettings.csv")


    counter = 0
    winstreak = True

    while winstreak:
        n = int(df.size/3)

        i = random.randint(0 ,n - 1)

        answer = input("The capital of " + df.iat[i,0] + " is ... " )

        #answer = string(answer)

        if answer == df.iat[i,1]:
            print("Correct, " + df.iat[i,1] + " is the capital city of " + df.iat[i,0] )
            counter = counter + 1
        else:
            winstreak = False


    print("You had " +  str(counter) + " options right!")

    if(counter > scores.iat[0,2]):
        scores.iat[0,2] = counter
        scores.to_csv("gamesettings.csv", index =False)
        print("Congrats, you have a new high score! " + str(counter) + "points")

    """

    Further functonalities of the game
     * Capital to country
     * Country to capital
     * include a map functionality with map of the country, with map in the world
     * include score that compares against global score
    set gamecode counter globally
     * include regex parsing for 1 different letter
    """


if __name__ == "__main__":
    """This runs when you execute '$ python3 mypackage/mymodule.py'"""
    game()
