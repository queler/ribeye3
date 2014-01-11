# RBI Baseball 3 - ROM Modifier
# Chet Collins
# November 2013



from PlayersData import *
from Validator import *
import binascii
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
            #print(self.data)
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
        data = ":(pitchers)DONT CHANGE,lineup# DONT CHANGE,Name,SinkerVal,Stance,ERA," \
               "SinkSpd,RegSpd,FastSpd,LCurve,RCurve,Stamina,CPU1,CPU2\n"
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
        data = ":(batters)DONT CHANGE,lineup# DONT CHANGE,Name,Stance,BA,HR,Contact," \
               "Power,Speed,FieldingPos,Switch\n"
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

    def display_team_params(self):
        """
        @return: A list of team parameters like error %, uniform colour options,
        """

    def write_file(self):
        FileProcessor().write_output(self.__str__())

    def write_game_file(self):
        FileProcessor().write_nes_file(self.data)

    def import_new_data(self):
        """
        Read in all Pitcher and Batter data from csv file
        @return:
        """
        new_data = FileProcessor().read_csv_file()

        for line in new_data:
            if ":(batters)" in line:
                read_in = "bats"
            if ":(pitchers)" in line:
                read_in = "pitch"

            if read_in == "bats" and ":(batters)" not in line:
                # split the .csv line into a small array
                values = [x.strip() for x in line.split(',')]
                # check if we have a valid Batter
                if not is_valid_batter(values):
                    for text in is_valid_batter(values):
                        print(text)
                else:
                    #print("Valid batter found!\n")
                    self.valid_batter_from_csv(values)

            if read_in == "pitch" and ":(pitchers)" not in line:
                # split the .csv line into a small array
                values = [x.strip() for x in line.split(',')]
                # check if we have a valid Pitcher
                if not is_valid_pitcher(values):
                    for text in is_valid_pitcher(values):
                        print(text)
                else:
                    #print("Valid pitcher found!\n")
                    self.valid_pitcher_from_csv(values)

        # re-initialize self.players based on new players
        self.players = PlayersData(self.data)

    def valid_pitcher_from_csv(self, values):
        # check for what teamID and decide what offset to use
        self.update_player(Pitcher(PlayerEditHelper().get_pitcher_offset(int(values[0]), int(values[1])),
                    int(values[1]), PlayerEditHelper().name_check(values[2]), int(values[3]), int(values[4]),
                    float(values[5]), int(values[6]), int(values[7]), int(values[8]), int(values[9]),
                    int(values[10]), int(values[11]), int(values[12]), int(values[13])))

    def valid_batter_from_csv(self, values):
        # check for what teamID and decide what offset to use
        self.update_player(Batter(PlayerEditHelper().get_batter_offset(int(values[0]), int(values[1])),
                    int(values[1]), PlayerEditHelper().name_check(values[2]), int(values[3]), int(values[4]),
                    int(values[5]), int(values[6]), int(values[7])%256, int(values[7])//256, int(values[8]),
                    int(values[9]), int(values[10])))

    def replace_player(self,string,offset):
        """
        @param string: Player to be replaced in the ROM file
        @param offset: address within the ROM file
        @return:
        """
        #remove print after debugging
        #print(str(offset)+" "+string)
        self.data = self.data[0:offset] + string + self.data[offset+PLAYER_LEN:]
        #print(self.data[offset:offset+PLAYER_LEN])

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






