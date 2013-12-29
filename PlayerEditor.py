# RBI Baseball 3 - ROM Modifier
# Chet Collins
# November 2013

# provides the ability to convert players to and from their hex strings, and update players on the ROM file

import Values as v
import binascii
from PlayerNames import *
from Batter import *
from Pitcher import *
game_file = ""      # see comments on this var in __init__


class PlayerEditor(object):
    names = PlayerNames()
    batters = {}
    pitchers = {}

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

    # string representation of the PlayerEditor object
    def __str__(self):
        return self.data
    
    # determine if line contains valid data
    def invalid_entry(self,data):
        return int(data,v.HEX_BASE) == 0

    # loads all pitchers from ROM file
    def get_pitcher_block(self,start,end):
        for offset in range(start,end,v.PLAYER_LEN):
            data = self.data[offset:(offset+v.PLAYER_LEN)]
            if not self.invalid_entry(data):
                self.pitchers[offset] = self.create_pitcher(data,offset)
                print(self.create_pitcher(data,offset))
                print(data)
                print(self.batter_convert(self.create_batter(data,offset)))

    # loads all batters from ROM file
    def get_batter_block(self,start,end):
        for offset in range(start,end,v.PLAYER_LEN):
            data = self.data[offset:(offset+v.PLAYER_LEN)]
            self.batters[offset] = self.create_batter(data,offset)
            print(self.create_batter(data,offset))
            print(data)
            print(self.pitcher_convert(self.create_pitcher(data,offset)))

    # testing that a player can be created and overwritten in the ROM file
    def test_update(self):
        data = self.data[v.BATTER_S1:(v.BATTER_S1+v.PLAYER_LEN)]
        batter1 = self.create_batter(data,v.BATTER_S1)
        batter1.name = "ARod    "
        batter1.batting_avg = 350
        batter1.home_runs = 50
        batter1.speed = 100

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

    # here is where ROM file changes are written.
    def replace_player(self,string,offset):
        self.data = self.data[0:offset] + string + self.data[offset+v.PLAYER_LEN:]
        # added these lines because when we open as a binary file, we need to manually write the changes.
        # (we can't just keep modifying "self" because the binascii.hexlify get in the way)
        # NOTE: the "modified_" prefix can be removed after testing; it is just preventing bad overwrites.
        with open("modified_" + game_file, "wb") as my_file:
            my_file.write(binascii.unhexlify(self.data))


    # update a player and write to ROM file
    def update_player(self,player):
        update_string = ""
        if isinstance(player,Batter):
            #print('Batter found!')
            update_string = self.batter_convert(player)
        elif isinstance(player,Pitcher):
            update_string = self.pitcher_convert(player)
            #print('Pitcher found!')

        self.replace_player(update_string,player.offset)


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
