# RBI Baseball 3 - ROM Modifier
# Chet Collins
# November 2013



from PlayersData import *
import Validator
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
        i = PITCHER_S1
        while i < PITCHER_E1:
            if not PlayerEditHelper().invalid_entry(PlayerEditHelper().get_substring(self.data,i)):
                data += FileProcessor().convert_csv(
                    str(PlayerEditHelper().get_team_id(self.players.pitchers[i])) + "\t" + str(self.players.pitchers[i]))
            i += PLAYER_LEN
        i = PITCHER_S2
        while i < PITCHER_E2:
            if not PlayerEditHelper().invalid_entry(PlayerEditHelper().get_substring(self.data,i)):
                data += FileProcessor().convert_csv(
                    str(PlayerEditHelper().get_team_id(self.players.pitchers[i])) + "\t" + str(self.players.pitchers[i]))
            i += PLAYER_LEN
        return data

    def display_batters(self):
        """
        @return: A list of Batters in order
        """
        data = ":(batters)\n"
        i = BATTER_S1
        while i < BATTER_E1:
            data += FileProcessor().convert_csv(
                str(PlayerEditHelper().get_team_id(self.players.batters[i])) + "\t" + str(self.players.batters[i]))
            i += PLAYER_LEN
        i = BATTER_S2
        while i < BATTER_E2:
            data += FileProcessor().convert_csv(
                str(PlayerEditHelper().get_team_id(self.players.batters[i])) + "\t" + str(self.players.batters[i]))
            i += PLAYER_LEN
        return data

    def write_file(self):
        FileProcessor().write_csv(self.data)

    def replace_player(self,string,offset):
        """
        @param string: Player to be replaced in the ROM file
        @param offset: address within the ROM file
        @return:
        """
        self.data = self.data[0:offset] + string + self.data[offset+PLAYER_LEN:]

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






