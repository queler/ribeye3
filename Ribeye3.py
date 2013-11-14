#!/usr/bin/python

# RBI Baseball 3 - ROM Modifier
# Chet Collins

import sys, argparse

# parse the command line arguments
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='inputFile')
    parser.add_argument('-o', dest='outputFile')
    args = parser.parse_args()
    return args


def search(text):


    player_names = {}


def main():
    file_object = parse_args()
    with open(file_object.inputFile, "r+") as my_file:
        data = my_file.read()
    search(data)


if __name__ == "__main__":
    main(sys.argv)