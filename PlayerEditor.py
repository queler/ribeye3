# RBI Baseball 3 - ROM Modifier
# Chet Collins
# November 2013

# provides the ability to convert players to and from their hex strings, and update players on the ROM file

import Values as v
from PlayerNames import *
from Batter import *
from Pitcher import *


class PlayerEditor(object):
    names = PlayerNames()
    batters = {}
    pitchers = {}

    def __init__(self,filename):
        # open the ROM file
        with open(filename, "r+") as my_file:
            self.data = my_file.read()

    # string representation of the PlayerEditor object
    def __str__(self):
        return self.data
    
    # determine if line contains valid data
    def valid_entry(self,data):
        return int(data,16) == 0

    # loads all pitchers from ROM file
    def get_pitcher_block(self,start,end):
        for offset in range(start,end,v.PLAYER_LEN):
            data = self.data[offset:(offset+v.PLAYER_LEN)]
            if not self.valid_entry(data):
                self.pitchers[offset] = self.create_pitcher(data,offset)
                print(self.create_pitcher(data,offset))
                #print(self.batter_convert(self.create_batter(data,offset))

    # loads all batters from ROM file
    def get_batter_block(self,start,end):
        for offset in range(start,end,v.PLAYER_LEN):
            data = self.data[offset:(offset+v.PLAYER_LEN)]
            self.batters[offset] = self.create_batter(data,offset)
            print(self.create_batter(data,offset))
            #print(self.pitcher_convert(self.create_pitcher(data,offset)))

    # load players from their defined memory addresses
    def load_players(self):
        # loading batters
        self.get_batter_block(v.BATTER_S1,v.BATTER_E1)
        self.get_batter_block(v.BATTER_S2,v.BATTER_E2)

        # loading pitchers
        self.get_pitcher_block(v.PITCHER_S1,v.PITCHER_E1)
        self.get_pitcher_block(v.PITCHER_S2,v.PITCHER_E2)

    # convert a hex value to an integer
    def hex_to_int(self,data,start,end):
        return int(data[start:end],v.HEX_BASE)

    # format a hex string to conform to ROM file standards
    def hex_format(self,value,precision):
        return str(hex(value)).lstrip('0x').zfill(precision).upper()

    # convert a batter to an equivalent hex string
    def batter_convert(self, batter):
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

    # convert a pitcher to an equivalent hex string
    def pitcher_convert(self, pitcher):
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


    # create a batter from ROM file
    def create_batter(self,data,offset):
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

    # create a pitcher from ROM file
    def create_pitcher(self,data,offset):
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
