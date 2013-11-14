#!/usr/bin/python

# RBI Baseball 3 - ROM Modifier
# Chet Collins

import sys,PlayerNames

game_file = "rbi3_game_file"

def main():
    # open the game file
    with open(game_file, "r+") as my_file:
        data = my_file.read()

    names = PlayerNames()

if __name__ == "__main__":
    main(sys.argv)