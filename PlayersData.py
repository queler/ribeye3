# RBI Baseball 3 - ROM Modifier
# Chet Collins
# November 2013

from PlayerEditHelper import *

class PlayersData():
    """ Abstraction of the list of all Pitchers and Batters
    """
    pitchers = {}
    batters = {}

    def __init__(self,data):
        self.load_players(data)

    def __str__(self):
        """
        @return: list of all Pitchers and Batters
        """
        return self.display_pitchers() + self.display_batters()

    #TODO fix the dirty hack below
    def display_pitchers(self):
        data = ""
        i = v.PITCHER_S1
        while i < v.PITCHER_E1:
            if not self.pitchers[i].name == "00000000":
                data += str(self.pitchers[i])
            i += v.PLAYER_LEN
        i = v.PITCHER_S2
        while i < v.PITCHER_E2:
            if not self.pitchers[i].name == "00000000":
                data += str(self.pitchers[i])
            i += v.PLAYER_LEN
        return data
            
    def display_batters(self):
        data = ""
        i = v.BATTER_S1
        while i < v.BATTER_E1:
            data += str(self.batters[i])
            i += v.PLAYER_LEN
        i = v.BATTER_S2
        while i < v.BATTER_E2:
            data += str(self.batters[i])
            i += v.PLAYER_LEN
        return data

    def get_pitcher_block(self,data,start,end):
        """
        Load all Pitchers from ROM file
        @param start: start address
        @param end: end address
        @return:
        """
        for offset in range(start,end,v.PLAYER_LEN):
            if not PlayerEditHelper().invalid_entry(data):
                self.pitchers[offset] = PlayerEditHelper().create_pitcher(data[offset:offset+v.PLAYER_LEN],offset)

    def get_batter_block(self, data, end, start):
        """
        Load all Batters from ROM file
        @param data: data from the ROM file
        @param start: start address
        @param end: end address
        @return:
        """
        for offset in range(start,end,v.PLAYER_LEN):
            self.batters[offset] = PlayerEditHelper().create_batter(data[offset:offset+v.PLAYER_LEN],offset)

    def load_players(self,data):
        """
        Load players from their defined memory addresses
        @return:
        """
        # loading batters
        self.get_batter_block(data, v.BATTER_E1, v.BATTER_S1)
        self.get_batter_block(data, v.BATTER_E2, v.BATTER_S2)

        # loading pitchers
        self.get_pitcher_block(data,v.PITCHER_S1,v.PITCHER_E1)
        self.get_pitcher_block(data,v.PITCHER_S2,v.PITCHER_E2)
