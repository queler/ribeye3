#!/usr/bin/python
# a representation of a batter from RBI3


class Batter():
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
        print(self.lineup_pos + '\t'+
            self.name + '\t'+
            self.stance + '\t'+
            self.batting_avg + '\t'+
            self.home_runs + '\t'+
            self.contact + '\t'+
            self.power + '\t'+
            self.speed + '\t'+
            self.position + '\t'+
            self.switch + '\n')




