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
        # load dictionary values from file
        with open(filename) as my_file:
            for line in my_file:
                key, value = line.partition("\t")[::2]
                self.dict[str(key)] = value.strip()

    # Given a hex string, return the string in alphanumeric form
    def search(self,hex_string):
        name = ""
        for (hex_part1,hex_part2) in zip(hex_string[0::2],hex_string[1::2]):
            hex_part1 += hex_part2
            name += self.dict[hex_part1]

        return name

def main():
    names = PlayerNames()
    print(names.dict.__str__())
    print(names.search('000A0B0C0D0E42312142'))

main()

