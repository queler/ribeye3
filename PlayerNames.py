# Two way map to relate alphanumeric characters and hex values


class PlayerNames(dict):
    filename = "player_name_map.txt"

    def __init__(self):
        super().__init__()
        # load dictionary values from file
        with open(self.filename) as my_file:
            for line in my_file:
                key, value = line.partition("\t")[::2]
                self.__setitem__(str(key).strip(), str(value).strip())

    def __len__(self):
        return dict.__len__(self)/2

    # two way dictionary function
    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        dict.__setitem__(self, value, key)

    # Given a hex string, return the alphanumeric equivalent
    def hex2alpha(self, hex_string):
        name = ""
        for (hex_part1,hex_part2) in zip(hex_string[0::2],hex_string[1::2]):
            hex_part1 += hex_part2
            name += self.get(hex_part1)
        return name

    # Given an alpha string, return the hex equivalent
    def alpha2hex(self, alpha_string):
        name = ""
        for char in alpha_string:
            name += self.get(char)
        return name




