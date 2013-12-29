# RBI Baseball 3 - ROM Modifier
# Chet Collins
# November 2013

# a representation of a batter from RBI3


class Batter(object):
    def __init__(self, offset, lineup_pos, name, stance, batting_avg, home_runs, contact, power1, power2, speed, position , switch):
        self.offset = offset
        self.lineup_pos = lineup_pos
        self.name = name
        self.stance = stance
        self.batting_avg = batting_avg
        self.home_runs = home_runs
        self.contact = contact
        self.power1 = power1
        self.power2 = power2
        self.power = power1 + (power2*256)
        self.speed = speed
        self.position = position
        self.switch = switch

    # a string representation of a batter
    def __str__(self):
        return(str(hex(self.offset//2)) + '\t' +
               str(self.lineup_pos) + '\t' +
               self.name + '\t' +
               str(self.stance) + '\t' +
               str(self.batting_avg) + '\t' +
               str(self.home_runs) + '\t' +
               str(self.contact) + '\t' +
               str(self.power) + '\t' +
               str(self.speed) + '\t' +
               str(self.position) + '\t' +
               str(self.switch) + '\n')


def testbatter():
    """
    test function. Creates instance of batter
    @return: NULL
    """
    batter = Batter(8, 8, "Bill", 8, 8, 8, 8, 8, 8, 8, 8, 8)
    assert batter.offset == 8
    assert batter.lineup_pos == 8
    assert batter.name == "Bill"
    assert batter.stance == 8
    assert batter.batting_avg == 8
    assert batter.home_runs == 8
    assert batter.contact == 8
    assert batter.power1 == 8
    assert batter.power2 == 8
    assert batter.power == 8 + (8*256)
    assert batter.speed == 8
    assert batter.position == 8
    assert batter.switch == 8
    return


def test__str__():
    batter = Batter(8, 8, "Bill", 8, 8, 8, 8, 8, 8, 8, 8, 8)
    # print(batter.__str__())
    return

testbatter()
test__str__()
