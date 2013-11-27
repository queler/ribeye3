#!/usr/bin/python

# RBI Baseball 3 - ROM Modifier
# Chet Collins

from PlayerNames import *
from Pitcher import *
from Batter import *
from PlayerEditor import *
game_file = "rbi3_game_file.txt"


def main():
    # open the game file
    with open(game_file, "r+") as my_file:
        data = my_file.read()

    names = PlayerNames()
    #print(names)
    #print(names.hex2alpha('000A0B0C0D0E4231214242'))
    #print(names.alpha2hex('McGwire'))

    #player1 = Batter(32,0,'McGwire',0,300,45,5,100,100,0,0)
    #player2 = Pitcher(32,2,'Clemens',100,1,10,10,10,10,10,60,10,10)
    #print(player1)
    #print(player2)

    editor = PlayerEditor(game_file)
    #print(editor)

    editor.load_players()
    #editor.display_players()



if __name__ == "__main__":
    main()