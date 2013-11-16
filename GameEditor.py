# mechanism to edit an RBI3 ROM file


class GameEditor(object):
    def __init__(self,filename):
        # open the game file
        with open(filename, "r+") as my_file:
            self.data = my_file.read()

    # string representation of the GameEditor object
    def __str__(self):
        return self.data


