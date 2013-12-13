# RBI Baseball 3 - ROM Modifier
# Chet Collins
# November 2013

""" Main program
"""

from PlayerEditor import *
game_file = "rom-files/rbi3_game_file.txt"


def main():
    editor = PlayerEditor(game_file)
    print(str(editor))
    editor.write_file()

if __name__ == "__main__":
    main()