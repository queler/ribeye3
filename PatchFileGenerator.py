# RBI Baseball 3 - ROM Modifier
# Brahm Neufeld
# December 2013

import time

original_1990_rom = "rbi3.txt"
modified_2013_rom = "rbi2013-v2-WIP.txt"

# function to compare two strings, print the positions
# and values of any DIFFERENCES
def character_compare(a,b):
    output = ""
    for i in range(len(a)):
        if a[i] != b[i]:
            print(i, b[i])
            output += str(i) + "\t" + str(b[i]) + "\n"
    return output

def main():

    with open(original_1990_rom, "r") as rom_1990:
        data_1990 = rom_1990.read()

    with open(modified_2013_rom, "r") as rom_2013:
        data_2013 = rom_2013.read()

    # just a check to see if the two files are equal
    # print(data_1990 == data_2013)

    with open(time.strftime("%Y-%m-%d_%H-%M-%S") + "-patch_file.txt", "w+") as f:
        f.write(character_compare(data_1990, data_2013))
        f.close()

if __name__ == "__main__":
    main()