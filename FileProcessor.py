# RBI Baseball 3 - ROM Modifier
# Chet Collins
# November 2013


class FileProcessor():
    """ Provides ability to read from, and write to csv files
    """
    output = "output.csv"
    input = "input.txt"

    def convert_csv(self,player):
        """
        @param player: A Batter or Pitcher
        @return: a csv-style string representing a Player
        """
        return ",".join(player.split('\t'))

    def write_output(self,data):
        """
        @param data: text to be written
        @return:
        """
        with open(self.output, "w+") as output_file:
            output_file.write(data)
            output_file.close()




