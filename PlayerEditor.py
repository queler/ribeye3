# RBI Baseball 3 - ROM Modifier
# Chet Collins
# November 2013

from PlayerEditHelper import *
from PlayersData import *

class PlayerEditor():
    """ Provides the ability to convert players to and from their hex strings, and update players on the ROM file
    """

    def __init__(self,filename):
        with open(filename, "r+") as my_file:
            self.data = my_file.read()

        # loading players from initial ROM data
        self.players = PlayersData(self.data)

    def __str__(self):
        """
        @return: list of all Pitchers and Batters
        """
        return self.display_pitchers() + self.display_batters()

    def display_pitchers(self):
        """
        @return: A list of Pitchers in order
        """
        data = ""
        i = v.PITCHER_S1
        while i < v.PITCHER_E1:
            if not PlayerEditHelper().invalid_entry(PlayerEditHelper().get_substring(self.data,i)):
                data += str(self.players.pitchers[i])
            i += v.PLAYER_LEN
        i = v.PITCHER_S2
        while i < v.PITCHER_E2:
            if not PlayerEditHelper().invalid_entry(PlayerEditHelper().get_substring(self.data,i)):
                data += str(self.players.pitchers[i])
            i += v.PLAYER_LEN
        return data

    def display_batters(self):
        """
        @return: A list of Batters in order
        """
        data = ""
        i = v.BATTER_S1
        while i < v.BATTER_E1:
            data += str(self.players.batters[i])
            i += v.PLAYER_LEN
        i = v.BATTER_S2
        while i < v.BATTER_E2:
            data += str(self.players.batters[i])
            i += v.PLAYER_LEN
        return data

    def replace_player(self,string,offset):
        """
        @param string: Player to be replaced in the ROM file
        @param offset: address within the ROM file
        @return:
        """
        self.data = self.data[0:offset] + string + self.data[offset+v.PLAYER_LEN:]


    def update_player(self,player):
        """
        Update a player and write to ROM file
        @param player: Player to be updated
        @return:
        """
        update_string = ""
        if isinstance(player,Batter):
            #print('Batter found!')
            update_string = PlayerEditHelper.batter_convert(player)
        elif isinstance(player,Pitcher):
            update_string = PlayerEditHelper.pitcher_convert(player)
            #print('Pitcher found!')
        self.replace_player(update_string,player.offset)



