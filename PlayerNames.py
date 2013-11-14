#!/usr/bin/python

"""
Dictionary containing the dictionary of hex value to alphanumeric character translation
key: hex value
value: alphanumeric character
"""

filename = "player_name_map.txt"

class PlayerNames:
    def __init__(self):
        self.dict = {}

        with open(filename) as my_file:
            for line in my_file:
                key, value = line.partition("\t")[::2]
                self.dict[key] = value.strip()


def main():
    names = PlayerNames()
    print(names.dict.__str__())

main()

