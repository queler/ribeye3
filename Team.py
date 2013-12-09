# RBI Baseball 3 - ROM Modifier
# Chet Collins
# November 2013

"""
TeamID
Team
Outline
Pitcher Pants
Jersey
Batter Offset
Pitcher Offset
Team Error%
Team Years
"""

class Team(object):
    """ A representation of Team in RBI3
    """
    def __init__(self,data_list):
        self.team_id = data_list[0]
        self.team_text = data_list[1]
        self.outline = data_list[2]
        self.pitcher_pants = data_list[3]
        self.jersey = data_list[4]
        self.batter_offset = data_list[5]
        self.pitcher_offset = data_list[6]
        self.team_error = data_list[7]
        self.team_years = data_list[8]

    def __str__(self):
        return str(self.team_id) + "\t" +\
        self.team_text + "\t"+\
        self.outline + "\t"+\
        self.pitcher_pants + '\t'+\
        self.jersey  + '\t'+\
        self.batter_offset + '\t'+\
        self.pitcher_offset + '\t'+\
        self.team_error + '\t'+\
        self.team_years


