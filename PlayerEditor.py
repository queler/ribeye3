# RBI Baseball 3 - ROM Modifier
# Chet Collins
# November 2013


import Values as v
from PlayerNames import *
from Batter import *
from Pitcher import *
from FileProcessor import *
from TeamsData import *


class PlayerEditor(object):
    """ Provides the ability to convert players to and from their hex strings, and update players on the ROM file
    """
    names = PlayerNames()
    file_process = FileProcessor()
    batters = {}
    pitchers = {}
    teams_data = TeamsData()

    def __init__(self,filename):
        with open(filename, "r+") as my_file:
            self.data = my_file.read()

    def __str__(self):
        """
        @return: a string containing the ROM file
        """
        return self.data

    def invalid_entry(self,data):
        """
        Test for a valid entry
        @param data: the entry to be tested
        @return: if line contains valid data
        """
        return int(data,v.HEX_BASE) == 0

    def get_pitcher_block(self,start,end):
        """
        Load all Pitchers from ROM file
        @param start: start address
        @param end: end address
        @return:
        """
        for offset in range(start,end,v.PLAYER_LEN):
            data = self.data[offset:(offset+v.PLAYER_LEN)]
            if not self.invalid_entry(data):
                self.pitchers[offset] = self.create_pitcher(data,offset)
                print(self.file_process.convert_csv(str(self.pitchers[offset])))

    def get_batter_block(self,start,end):
        """
        Load all Batters from ROM file
        @param start: start address
        @param end: end address
        @return:
        """
        for offset in range(start,end,v.PLAYER_LEN):
            data = self.data[offset:(offset+v.PLAYER_LEN)]
            self.batters[offset] = self.create_batter(data,offset)
            print(self.file_process.convert_csv(str(self.batters[offset])))

    def load_players(self):
        """
        Load players from their defined memory addresses
        @return:
        """
        # loading batters
        self.get_batter_block(v.BATTER_S1,v.BATTER_E1)
        self.get_batter_block(v.BATTER_S2,v.BATTER_E2)

        # loading pitchers
        self.get_pitcher_block(v.PITCHER_S1,v.PITCHER_E1)
        self.get_pitcher_block(v.PITCHER_S2,v.PITCHER_E2)

        # print teams data
        print(self.teams_data)


    def hex_to_int(self,data,start,end):
        """
        Convert a hex value to an integer
        @param data: the hex string containing data
        @param start: start index
        @param end: end index
        @return: the integer value
        """
        return int(data[start:end],v.HEX_BASE)

    def hex_format(self,value,precision):
        """
        format a hex string to conform to ROM file standards
        @param value: hex string to be formatted
        @param precision: number of decimal places
        @return: a formatted hex string
        """
        return str(hex(value)).lstrip('0x').zfill(precision).upper()

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
            update_string = self.batter_convert(player)
        elif isinstance(player,Pitcher):
            update_string = self.pitcher_convert(player)
            #print('Pitcher found!')

        self.replace_player(update_string,player.offset)


    def batter_convert(self, batter):
        """
        Convert a batter to an equivalent hex string
        @param batter: Batter to convert
        @return: a Batter converted from hex
        """
        return self.hex_format(batter.lineup_pos,2) + \
        self.names.alpha_to_hex(batter.name[:6]) + \
        self.hex_format(batter.stance,2) + \
        self.hex_format(batter.batting_avg-111,2) + \
        self.hex_format(batter.home_runs,2) + \
        self.hex_format(batter.contact,2) + \
        self.hex_format(batter.power1,2) + \
        self.hex_format(batter.power2,2) + \
        self.hex_format(batter.speed,2) + \
        self.hex_format(batter.position,2) + \
        self.hex_format(batter.switch,2) + \
        self.names.alpha_to_hex(batter.name[6:])

    def pitcher_convert(self, pitcher):
        """ 
        Convert a Pitcher to an equivalent hex string
        @param pitcher: Pitcher to convert
        @return: a Pitcher converted from hex
        """
        return self.hex_format(pitcher.staff_pos,2) + \
        self.names.alpha_to_hex(pitcher.name[:6]) + \
        self.hex_format(pitcher.sinker_val,1) + \
        self.hex_format(pitcher.style,1) + \
        self.hex_format(pitcher.mystery,2) + \
        self.hex_format(pitcher.sink_spd,2) + \
        self.hex_format(pitcher.reg_spd,2) + \
        self.hex_format(pitcher.fast_spd,2) + \
        self.hex_format(pitcher.left_curve,1) + \
        self.hex_format(pitcher.right_curve,1)+ \
        self.hex_format(pitcher.stamina,2) + \
        self.hex_format(pitcher.cpu_field1,2) + \
        self.hex_format(pitcher.cpu_field2,2)+ \
        self.names.alpha_to_hex(pitcher.name[6:])


    def create_batter(self,data,offset):
        """ 
        create a Batter from ROM file
        @param data: hex Batter data
        @param offset: starting address in ROM file
        @return: a new Batter 
        """
        lineup_pos = self.hex_to_int(data,0,2)
        name = self.names.hex_to_alpha(data[2:14]+data[32:36])
        stance = self.hex_to_int(data,14,16)
        batting_avg = 111+self.hex_to_int(data,16,18)
        home_runs = self.hex_to_int(data,18,20)
        contact = self.hex_to_int(data,20,22)
        power1 = self.hex_to_int(data,22,24)
        power2 = self.hex_to_int(data,24,26)
        speed = self.hex_to_int(data,26,28)
        position = self.hex_to_int(data,28,30)
        switch = self.hex_to_int(data,30,32)
        return Batter(offset,lineup_pos,name,stance,batting_avg,home_runs,contact,power1, power2,speed,position,switch)

    def create_pitcher(self,data,offset):
        """ 
        create a Pitcher from ROM file
        @param data: hex Pitcher data
        @param offset: starting address in ROM file
        @return: a new Pitcher 
        """
        staff_pos = self.hex_to_int(data,0,2)
        name = self.names.hex_to_alpha(data[2:14]+data[32:36])
        sinker_val = self.hex_to_int(data,14,15)
        style = self.hex_to_int(data,15,16)
        mystery = self.hex_to_int(data,16,18)
        sink_spd = self.hex_to_int(data,18,20)
        reg_spd = self.hex_to_int(data,20,22)
        fast_spd = self.hex_to_int(data,22,24)
        left_curve = self.hex_to_int(data,24,25)
        right_curve = self.hex_to_int(data,25,26)
        stamina = self.hex_to_int(data,26,28)
        cpu_field1 = self.hex_to_int(data,28,30)
        cpu_field2 = self.hex_to_int(data,30,32)
        return Pitcher(offset,staff_pos,name,sinker_val,style,mystery,sink_spd,reg_spd,fast_spd,left_curve,right_curve,stamina,cpu_field1,cpu_field2)
