# RBI Baseball 3 - ROM Modifier
# Brahm Neufeld
# January 2014

"""
Command-line support for RibEye3-Modifier
to do:
- prompt to: update ROM or create patchfile
- prompt to: export .csv from ROM file.
"""

from PlayerEditor import *
from PatchFileGenerator import *

def run_from_command_line():

    print("Hello!\n\n"
          "Welcome to the RibEye3-Modifier Program.\n\n"
          "This program will patch the original 1990 R.B.I. Baseball 3 ROM \nto a new 30-team version!\n"
          "\n"
          "Please ensure all files you will be prompted for are stored in \nthe \data_files subdirectory.\n"
          "\n")

    ready_to_begin = raw_input("Ready to begin (y/n)? ")

    if ready_to_begin.lower() == "y":
        print("Great!\n"
              "The first thing we need is the filename of the original 1990 ROM.\n")
        original_1990_rom = raw_input("1990 ROM filename: ")
        print("Excellent.\n"
              "The next thing we need is the filename of the .csv file of roster changes.\n")
        csv_file = raw_input(".csv filename: ")

        print("Ok, fantastic. \n"
              "The last detail we need is a new filename (ending in .nes) for your modified file.\n")
        new_filename = raw_input("What's it going to be? ")

        print("Patching 1990 ROM to modified 30-team version...\n")
        modify_1990_file("data_files\\"+original_1990_rom, "data_files\\2013patchfile.pch", "data_files\\" + new_filename)

        print("Opening patched ROM as new editor object...\n")
        editor = PlayerEditor("data_files\\"+new_filename)

        print("Importing data into ROM from .csv file...\n")
        editor.import_new_data("data_files\\" + csv_file)

        print("Writing to new ROM file...\n")
        editor.write_game_file("data_files\\"+new_filename)

        print("All done! Your ROM file is ready to use. ")


