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