# RBI Baseball 3 - ROM Modifier
# Chet Collins
# November 2013



import Values as v
import binascii
from PlayerNames import *
from Batter import *
from Pitcher import *
from PlayersData import *
game_file = ""      # see comments on this var in __init__

class PlayerEditor():
    """ Provides the ability to convert players to and from their hex strings, and update players on the ROM file
    """
    def __init__(self,filename):
        # open the ROM file - changed to read in binary mode, so we can open a .nes file. Also changed to read-only.
        with open(filename, "rb") as my_file:
            # str(binascii.hexlify()) creates a text string of hex, as if we'd opened a .txt file.
            # the rstrip and lstrip take out the binary "b" prefix and single quote marks that get added
            # upper() will make all of the hex uppercase; this plays nice with the character lookup
            self.data = str(binascii.hexlify(my_file.read())).rstrip("'").lstrip("b'").upper()
            # global variables are bad, any smart ideas to get this filename to the replace_player() function?
            global game_file
            game_file = filename

        # loading players from initial ROM data
        self.players = PlayersData(self.data)

    def __str__(self):
        """
        @return: list of all Pitchers and Batters
        """
        return self.display_batters() + self.display_pitchers()

    def display_pitchers(self):
        """
        @return: A list of Pitchers in order
        """
        data = ":(pitchers)\n"
        i = v.PITCHER_S1
        while i < v.PITCHER_E1:
            if not PlayerEditHelper().invalid_entry(PlayerEditHelper().get_substring(self.data,i)):
                data += FileProcessor().convert_csv(
                    str(PlayerEditHelper().get_team_id(self.players.pitchers[i])) + "\t" + str(self.players.pitchers[i]))
            i += v.PLAYER_LEN
        i = v.PITCHER_S2
        while i < v.PITCHER_E2:
            if not PlayerEditHelper().invalid_entry(PlayerEditHelper().get_substring(self.data,i)):
                data += FileProcessor().convert_csv(
                    str(PlayerEditHelper().get_team_id(self.players.pitchers[i])) + "\t" + str(self.players.pitchers[i]))
            i += v.PLAYER_LEN
        return data

    def display_batters(self):
        """
        @return: A list of Batters in order
        """
        data = ":(batters)\n"
        i = v.BATTER_S1
        while i < v.BATTER_E1:
            data += FileProcessor().convert_csv(
                str(PlayerEditHelper().get_team_id(self.players.batters[i])) + "\t" + str(self.players.batters[i]))
            i += v.PLAYER_LEN
        i = v.BATTER_S2
        while i < v.BATTER_E2:
            data += FileProcessor().convert_csv(
                str(PlayerEditHelper().get_team_id(self.players.batters[i])) + "\t" + str(self.players.batters[i]))
            i += v.PLAYER_LEN
        return data

    def write_file(self):
        FileProcessor().write_output(str(self))

        self.update_player(batter1)
        print(batter1)
        data2 = self.data[v.BATTER_S1:(v.BATTER_S1+v.PLAYER_LEN)]
        print(self.create_batter(data2,v.BATTER_S1))

    # load players from their defined memory addresses
    def load_players(self):
        # loading batters
        self.get_batter_block(v.BATTER_S1,v.BATTER_E1)
        self.get_batter_block(v.BATTER_S2,v.BATTER_E2)

        # loading pitchers
        self.get_pitcher_block(v.PITCHER_S1,v.PITCHER_E1)
        self.get_pitcher_block(v.PITCHER_S2,v.PITCHER_E2)

        self.test_update()

    # convert a hex value to an integer
    def hex_to_int(self,data,start,end):
        return int(data[start:end],v.HEX_BASE)

    # format a hex string to conform to ROM file standards
    def hex_format(self,value,precision):
        return str(hex(value)).lstrip('0x').zfill(precision).upper()

    def replace_player(self,string,offset):
        """
        @param string: Player to be replaced in the ROM file
        @param offset: address within the ROM file
        @return:
        """
        self.data = self.data[0:offset] + string + self.data[offset+v.PLAYER_LEN:]
        # added these lines because when we open as a binary file, we need to manually write the changes.
        # (we can't just keep modifying "self" because the binascii.hexlify get in the way)
        # NOTE: the "modified_" prefix can be removed after testing; it is just preventing bad overwrites.
        with open("modified_" + game_file, "wb") as my_file:
            my_file.write(binascii.unhexlify(self.data))

    def update_player(self,player):
        """
        Update a player and write to ROM file
        @param player: Player to be updated
        @return:
        """
        update_string = ""
        if isinstance(player,Batter):
            #print('Batter found!')
            update_string = PlayerEditHelper().batter_convert(player)
        elif isinstance(player,Pitcher):
            update_string = PlayerEditHelper().pitcher_convert(player)
            #print('Pitcher found!')
        self.replace_player(update_string,player.offset)



