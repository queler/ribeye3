# a representation of a batter from RBI3


class Batter(object):
    def __init__(self,lineup_pos,name,stance,batting_avg,home_runs,contact,power,speed,position,switch):
        self.lineup_pos = lineup_pos
        self.name = name
        self.stance = stance
        self.batting_avg = batting_avg
        self.home_runs = home_runs
        self.contact = contact
        self.power = power
        self.speed = speed
        self.position = position
        self.switch = switch

    # a string representation of a batter
    def __str__(self):
        return(str(self.lineup_pos) + '\t'+
            self.name + '\t'+
            str(self.stance) + '\t'+
            str(self.batting_avg) + '\t'+
            str(self.home_runs) + '\t'+
            str(self.contact) + '\t'+
            str(self.power) + '\t'+
            str(self.speed) + '\t'+
            str(self.position) + '\t'+
            str(self.switch) + '\n')





