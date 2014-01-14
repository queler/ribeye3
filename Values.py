# Constant address values and sizes
HEX_BASE = 16

# size of each player object
PLAYER_LEN = 36
NAME_LEN = 8
PITCHERS_PER_TEAM = 10
BATTERS_PER_TEAM = 14

# start and end addresses of Batter and Pitcher blocks
BATTER_S1 = int('0010',16)*2
BATTER_E1 = int('01D97',16)*2
BATTER_S2 = int('16010',16)*2
BATTER_E2 = int('17D98',16)*2
PITCHER_S1 = int('12010',16)*2
PITCHER_E1 = int('13D4F',16)*2
PITCHER_S2 = int('18010',16)*2
PITCHER_E2 = int('19D4F',16)*2

# start and end of ERA pitching tables (**2005/2013 ROM** - ROM file must be patched prior to running ERA changes)
ERA_DIGITS12_S1 = int('19D88',16)*2
ERA_DIGITS12_E1 = int('19E57',16)*2
ERA_DIGIT3_S1 = int('19F48',16)*2
ERA_DIGIT3_E1 = int('19FAF',16)*2


# Validation for Team, Pitcher, and Batters

# Team value ranges
TEAM_ID_MIN = 1
TEAM_ID_MAX = 60

# Pitcher value ranges
PITCHER_MIN = 0
STAFF_POS_START = 14
STAFF_POS_END = 23
PITCH_ABILITY_MAX = 15
STYLE_MAX = 3
PITCH_SPD_MAX = 255
STAMINA_MAX = 255

# Batter value ranges
BATTER_MIN = 0
LINEUP_POS_END = 13
STANCE_MAX = 1
BATTING_AVG_MAX = 366
HOME_RUN_MAX = 55
CONTACT_MAX = 99
POWER_MAX = 1100
SPEED_MAX = 255
FIELD_POS_MAX = 2
SWITCH_HITTER = 1


