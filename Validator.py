from Values import *

def validate_pitcher(self,data):
    """ Ensure that a Pitcher has valid data before creating object
    @param data: the Pitcher data to be validated
    @return: whether the data is valid
    """
    error_msg = data + '\n'
    status = True

    if TEAM_ID_MIN <= data[0] <= TEAM_ID_MAX:
        error_msg += "Team Id: %i must be within %i and %i\n",data[0],TEAM_ID_MIN,TEAM_ID_MAX
        status = False
    if STAFF_POS_START <= data[1] <= STAFF_POS_END:
        error_msg += "Staff Pos: %i must be within %i and %i\n",data[1],STAFF_POS_START,STAFF_POS_END
        status = False
    if data[2] > PLAYER_LEN:
        error_msg += "Name: %s must be within %i characters\n",data[2],PLAYER_LEN
        status = False
    if PITCHER_MIN <= data[3] <= PITCH_ABILITY_MAX:
        error_msg += "Sinker Val: %i must be within %i and %i\n",data[3],PITCHER_MIN,PITCH_ABILITY_MAX
        status = False
    if PITCHER_MIN <= data[4] <= STYLE_MAX:
        error_msg += "Style: %i must be within %i and %i\n",data[4],PITCHER_MIN,STYLE_MAX
        status = False
    if PITCHER_MIN <= data[5] <= PITCH_SPD_MAX:
        error_msg += "Sinker Spd: %i must be within %i and %i\n",data[5],PITCHER_MIN,PITCH_SPD_MAX
        status = False
    if PITCHER_MIN <= data[6] <= PITCH_SPD_MAX:
        error_msg += "Regular Spd: %i must be within %i and %i\n",data[6],PITCHER_MIN,PITCH_SPD_MAX
        status = False
    if PITCHER_MIN <= data[7] <= PITCH_SPD_MAX:
        error_msg += "Fastball Spd: %i must be within %i and %i\n",data[7],PITCHER_MIN,PITCH_SPD_MAX
        status = False
    if PITCHER_MIN <= data[8] <= PITCH_ABILITY_MAX:
        error_msg += "L Curve: %i must be within %i and %i\n",data[8],PITCHER_MIN,PITCH_ABILITY_MAX
        status = False
    if PITCHER_MIN <= data[9] <= PITCH_ABILITY_MAX:
        error_msg += "R Curve: %i must be within %i and %i\n",data[9],PITCHER_MIN,PITCH_ABILITY_MAX
        status = False
    if PITCHER_MIN <= data[10] <= PITCH_SPD_MAX:
        error_msg += "Stamina: %i must be within %i and %i\n",data[10],PITCHER_MIN,PITCH_SPD_MAX
        status = False
    return status, error_msg

def validate_batter(self,data):
    """ Ensure that a Batter has valid data before creating object
    @param data: the Batter data to be validated
    @return: whether the data is valid
    """
    error_msg = data + '\n'
    status = True

    if TEAM_ID_MIN <= data[0] <= TEAM_ID_MAX:
        error_msg += "Team Id: %i must be within %i and %i\n",data[0],TEAM_ID_MIN,TEAM_ID_MAX
        status = False
    if BATTER_MIN <= data[1] <= LINEUP_POS_END:
        error_msg += "Lineup Pos: %i must be within %i and %i\n",data[1],BATTER_MIN,LINEUP_POS_END
        status = False
    if data[2] > PLAYER_LEN:
        error_msg += "Name: %s must be within %i characters\n",data[2],PLAYER_LEN
        status = False
    if BATTER_MIN <= data[3] <= STANCE_MAX:
        error_msg += "Stance: %i must be within %i and %i\n",data[3],BATTER_MIN,STANCE_MAX
        status = False
    if BATTER_MIN <= data[4] <= BATTING_AVG_MAX:
        error_msg += "Batting Avg: %i must be within %i and %i\n",data[4],BATTER_MIN,BATTING_AVG_MAX
        status = False
    if BATTER_MIN <= data[5] <= HOME_RUN_MAX:
        error_msg += "Home Runs: %i must be within %i and %i\n",data[5],BATTER_MIN,HOME_RUN_MAX
        status = False
    if BATTER_MIN <= data[6] <= CONTACT_MAX:
        error_msg += "Contact: %i must be within %i and %i\n",data[6],BATTER_MIN,CONTACT_MAX
        status = False
    if BATTER_MIN <= data[7] <= POWER_MAX:
        error_msg += "Power: %i must be within %i and %i\n",data[7],BATTER_MIN,POWER_MAX
        status = False
    if BATTER_MIN <= data[8] <= SPEED_MAX:
        error_msg += "Speed: %i must be within %i and %i\n",data[8],BATTER_MIN,SPEED_MAX
        status = False
    if BATTER_MIN <= data[9] <= FIELD_POS_MAX:
        error_msg += "Position: %i must be within %i and %i\n",data[9],BATTER_MIN,FIELD_POS_MAX
        status = False
    if BATTER_MIN <= data[10] <= SWITCH_HITTER:
        error_msg += "Switch: %i must be within %i and %i\n",data[10],BATTER_MIN,SWITCH_HITTER
        status = False
    return status, error_msg