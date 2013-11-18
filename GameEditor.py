# mechanism to edit an RBI3 ROM file

import Values as v
from PlayerNames import *
from Batter import *
from Pitcher import *


class GameEditor(object):
    # character to hex map for PlayerNames
    names = PlayerNames()

    def __init__(self,filename):
        # open the game file
        with open(filename, "r+") as my_file:
            self.data = my_file.read()

    # string representation of the GameEditor object
    def __str__(self):
        return self.data

    def load_players(self):

        # first block of batters
        for offset in range(v.BATTER_S1,v.BATTER_E1,v.PLAYER_LEN):
            data = self.data[offset:(offset+v.PLAYER_LEN)]
            #print(self.create_batter(data,offset))

        # second block of batters
        for offset in range(v.BATTER_S2,v.BATTER_E2,v.PLAYER_LEN):
            data = self.data[offset:(offset+v.PLAYER_LEN)]
            #print(self.create_batter(data,offset))

        # first block of pitchers
        for offset in range(v.PITCHER_S1,v.PITCHER_E1,v.PLAYER_LEN):
            data = self.data[offset:(offset+v.PLAYER_LEN)]
            print(self.create_pitcher(data,offset))

        # second block of pitchers
        for offset in range(v.PITCHER_S2,v.PITCHER_E2,v.PLAYER_LEN):
            data = self.data[offset:(offset+v.PLAYER_LEN)]
            print(self.create_pitcher(data,offset))

    def hex_convert(self,data,start,end):
        return int(data[start:end],v.HEX_BASE)

    def create_batter(self,data,offset):
        lineup_pos = self.hex_convert(data,0,2)
        name = self.names.hex2alpha(data[2:14]+data[32:36])
        stance = self.hex_convert(data,14,16)
        batting_avg = 111+self.hex_convert(data,16,18)
        home_runs = self.hex_convert(data,18,20)
        contact = self.hex_convert(data,20,22)
        power = self.hex_convert(data,22,24)+(256*self.hex_convert(data,24,26))
        speed = self.hex_convert(data,26,28)
        position = self.hex_convert(data,28,30)
        switch = self.hex_convert(data,30,32)
        return Batter(offset,lineup_pos,name,stance,batting_avg,home_runs,contact,power,speed,position,switch)


    def create_pitcher(self,data,offset):
        staff_pos = self.hex_convert(data,0,2)
        name = self.names.hex2alpha(data[2:14]+data[32:36])
        sinker_val = self.hex_convert(data,14,15)
        style = self.hex_convert(data,15,16)
        sink_spd = self.hex_convert(data,18,20)
        reg_spd = self.hex_convert(data,20,22)
        fast_spd = self.hex_convert(data,22,24)
        left_curve = self.hex_convert(data,24,25)
        right_curve = self.hex_convert(data,25,26)
        stamina = self.hex_convert(data,26,28)
        cpu_field1 = self.hex_convert(data,28,30)
        cpu_field2 = self.hex_convert(data,30,32)
        return Pitcher(offset,staff_pos,name,sinker_val,style,sink_spd,reg_spd,fast_spd,left_curve,right_curve,stamina,cpu_field1,cpu_field2)
