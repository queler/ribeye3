# RBI Baseball 3 - ROM Modifier
# Chet Collins
# November 2013

""" Main program
"""

from PlayerEditor import *
from Values import *
from CmdLineSupport import *

# game_file = "rbi2013-1.3.nes"  # should be .nes file

def main():
    run_from_command_line()

    #editor = PlayerEditor(game_file)

    # read the csv file
    #editor.import_new_data()

    # try printing the first pitcher
    #print(PITCHER_S2)
    #print("196640 - "+ str(editor.players.pitchers[PITCHER_S2]))

    # print the whole gamefile
    #print(editor)

    # try printing the first pitcher
    #print("180256 - "+ str(editor.players.batters[180256]))

    # create a new instance of a pitcher - spaces added to make the padding work.
    #test_pitcher = Pitcher(PITCHER_S1,14,'Brahm   ',7,1,3.21,155,155,155,5,3,65,115,115)

    # this SHOULD insert my test pitcher into the editor object.
    #editor.players.pitchers[PITCHER_S1] = test_pitcher

    # print a test string to show the test_pitcher variable
    #print(str(test_pitcher))

    # print to show that the test_pitcher is inside of the editor object.
    #print(str(editor.players.pitchers[PITCHER_S1]))

    # print the hex representation of the test_pitcher
    #print(PlayerEditHelper().pitcher_convert(test_pitcher))

    # write the output csv file
    #editor.write_file()

    # write the game file
    #editor.write_game_file()

if __name__ == "__main__":
    main()