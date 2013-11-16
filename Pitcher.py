#!/usr/bin/python
# a representation of a pitcher from RBI3


class Pitcher():
    def __init__(self,staff_pos,name,sinker_val,style,sink_spd,reg_spd,fast_spd,left_curve,right_curve,stamina,cpu_field1,cpu_field2):
        self.staff_pos = staff_pos
        self.name = name
        self.sinker_val = sinker_val
        self.style = style
        self.sink_spd = sink_spd
        self.reg_spd = reg_spd
        self.fast_spd = fast_spd
        self.left_curve = left_curve
        self.right_curve = right_curve
        self.stamina = stamina
        self.cpu_field1 = cpu_field1
        self.cpu_field2 = cpu_field2

    # a string representation of a pitcher
    def __str__(self):
        print(self.staff_pos + '\t'+
            self.name + '\t'+
            self.sinker_val + '\t'+
            self.style + '\t'+
            self.sink_spd + '\t'+
            self.reg_spd + '\t'+
            self.fast_spd + '\t'+
            self.left_curve + '\t'+
            self.right_curve + '\t'+
            self.stamina + '\t'+
            self.cpu_field1 + '\t'+
            self.cpu_field2 + '\n')
