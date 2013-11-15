#!/usr/bin/python

# RBI Baseball 3 - ROM Modifier
# Chet Collins

import sys,PlayerNames

game_file = "rbi3_game_file.txt"

def main():
    # open the game file
    with open(game_file, "r+") as my_file:
        data = my_file.read()

    names = PlayerNames.PlayerNames()
    print(names.__str__())
    print(names.hex2alpha('000A0B0C0D0E4231214242'))
    print(names.alpha2hex('McGwire'))


if __name__ == "__main__":
    main()