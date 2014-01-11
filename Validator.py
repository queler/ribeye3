from Values import *

def is_valid_team(data):
    """
    Ensure that a team has valid data before creating an object.
    @param data: the team data to be validated
    @return: whether the team is valud, and error logging information
    TO DO: ACTUALLY COMPLETE ALL OF THIS TEAM DATA VALIDATION!!!
    """
    error_msg = ",".join(data)+'\n'
    status = True

    if TEAM_ID_MIN <= int(data[0]) <= TEAM_ID_MAX:
        error_msg += "Team Id: {0} must be within {1} and {2}\n".format(data[0],TEAM_ID_MIN,TEAM_ID_MAX)
        status = False



def is_valid_pitcher(data):
    """ Ensure that a Pitcher has valid data before creating object
    @param data: the Pitcher data to be validated
    @return: whether the Pitcher is valid, and the error logging information
    """
    error_msg = ",".join(data)+'\n'
    status = True

    if TEAM_ID_MIN <= int(data[0]) <= TEAM_ID_MAX:
        error_msg += "Team Id: {0} must be within {1} and {2}\n".format(data[0],TEAM_ID_MIN,TEAM_ID_MAX)
        status = False
    if STAFF_POS_START <= int(data[1]) <= STAFF_POS_END:
        error_msg += "Staff Pos: {0} must be within {1} and {2}\n".format(data[1],STAFF_POS_START,STAFF_POS_END)
        status = False
    if len(data[2]) > PLAYER_LEN:
        error_msg += "Name: {0} must be within {1} characters\n".format(data[2],PLAYER_LEN)
        status = False
    if PITCHER_MIN <= int(data[3]) <= PITCH_ABILITY_MAX:
        error_msg += "Sinker Val: {0} must be within {1} and {2}\n".format(data[3],PITCHER_MIN,PITCH_ABILITY_MAX)
        status = False
    if PITCHER_MIN <= int(data[4]) <= STYLE_MAX:
        error_msg += "Style: {0} must be within {1} and {2}\n".format(data[4],PITCHER_MIN,STYLE_MAX)
        status = False
    if PITCHER_MIN <= int(data[6]) <= PITCH_SPD_MAX:
        error_msg += "Sinker Spd: {0} must be within {1} and {2}\n".format(data[6],PITCHER_MIN,PITCH_SPD_MAX)
        status = False
    if PITCHER_MIN <= int(data[7]) <= PITCH_SPD_MAX:
        error_msg += "Regular Spd: {0} must be within {1} and {2}\n".format(data[7],PITCHER_MIN,PITCH_SPD_MAX)
        status = False
    if PITCHER_MIN <= int(data[8]) <= PITCH_SPD_MAX:
        error_msg += "Fastball Spd: {0} must be within {1} and {2}\n".format(data[8],PITCHER_MIN,PITCH_SPD_MAX)
        status = False
    if PITCHER_MIN <= int(data[9]) <= PITCH_ABILITY_MAX:
        error_msg += "L Curve: {0} must be within {1} and {2}\n".format(data[9],PITCHER_MIN,PITCH_ABILITY_MAX)
        status = False
    if PITCHER_MIN <= int(data[10]) <= PITCH_ABILITY_MAX:
        error_msg += "R Curve: {0} must be within {1} and {2}\n".format(data[10],PITCHER_MIN,PITCH_ABILITY_MAX)
        status = False
    if PITCHER_MIN <= int(data[11]) <= PITCH_SPD_MAX:
        error_msg += "Stamina: {0} must be within {1} and {2}\n".format(data[11],PITCHER_MIN,PITCH_SPD_MAX)
        status = False
    return status, error_msg

def is_valid_batter(data):
    """ Ensure that a Batter has valid data before creating object
    @param data: the Batter data to be validated
    @return: whether the Batter is valid, and the error logging information
    """
    error_msg = ",".join(data)+'\n'
    status = True

    if TEAM_ID_MIN <= int(data[0]) <= TEAM_ID_MAX:
        error_msg += "Team Id: {0} must be within {1} and {2}\n".format(int(data[0]),TEAM_ID_MIN,TEAM_ID_MAX)
        status = False
    if BATTER_MIN <= int(data[1]) <= LINEUP_POS_END:
        error_msg += "Lineup Pos: {0} must be within {1} and {2}\n".format(data[1],BATTER_MIN,LINEUP_POS_END)
        status = False
    if len(data[2]) > PLAYER_LEN:
        error_msg += "Name: {0} must be within {1} characters\n".format(data[2],PLAYER_LEN)
        status = False
    if BATTER_MIN <= int(data[3]) <= STANCE_MAX:
        error_msg += "Stance: {0} must be within {1} and {2}\n".format(data[3],BATTER_MIN,STANCE_MAX)
        status = False
    if BATTER_MIN <= int(data[4]) <= BATTING_AVG_MAX:
        error_msg += "Batting Avg: {0} must be within {1} and {2}\n".format(data[4],BATTER_MIN,BATTING_AVG_MAX)
        status = False
    if BATTER_MIN <= int(data[5]) <= HOME_RUN_MAX:
        error_msg += "Home Runs: {0} must be within {1} and {2}\n".format(data[5],BATTER_MIN,HOME_RUN_MAX)
        status = False
    if BATTER_MIN <= int(data[6]) <= CONTACT_MAX:
        error_msg += "Contact: {0} must be within {1} and {2}\n".format(data[6],BATTER_MIN,CONTACT_MAX)
        status = False
    if BATTER_MIN <= int(data[7]) <= POWER_MAX:
        error_msg += "Power: {0} must be within {1} and {2}\n".format(data[7],BATTER_MIN,POWER_MAX)
        status = False
    if BATTER_MIN <= int(data[8]) <= SPEED_MAX:
        error_msg += "Speed: {0} must be within {1} and {2}\n".format(data[8],BATTER_MIN,SPEED_MAX)
        status = False
    if BATTER_MIN <= int(data[9]) <= FIELD_POS_MAX:
        error_msg += "Position: {0} must be within {1} and {2}\n".format(data[9],BATTER_MIN,FIELD_POS_MAX)
        status = False
    if BATTER_MIN <= int(data[10]) <= SWITCH_HITTER:
        error_msg += "Switch: {0} must be within {1} and {2}\n".format(data[10],BATTER_MIN,SWITCH_HITTER)
        status = False
    return status, error_msg