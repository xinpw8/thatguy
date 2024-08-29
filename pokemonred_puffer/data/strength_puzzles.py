STRENGTH_SOLUTIONS = {}

boulder_1_to_2 = ['LEFT', 'LEFT', 'DOWN', 'LEFT', 'DOWN', 'DOWN', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'DOWN', 'LEFT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'UP', 'UP', 'UP', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'DOWN', 'DOWN', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'UP', 'LEFT', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'DOWN', 'RIGHT', 'DOWN', 'RIGHT', 'RIGHT', 'DOWN', 'DOWN']
boulder_2_to_3 = ['RIGHT', 'RIGHT', 'UP', 'UP', 'UP', 'UP', 'UP', 'RIGHT', 'UP', 'UP', 'RIGHT', 'UP', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'RIGHT', 'RIGHT', 'DOWN', 'DOWN', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'UP', 'UP', 'UP', 'UP', 'UP', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'UP', 'UP', 'UP', 'UP', 'LEFT', 'UP', 
                  'UP', 'UP']
boulder_3_to_4 = ['UP', 'UP', 'UP', 'UP', 'UP', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'DOWN', 'LEFT', 'DOWN']
active_strength_to_next_boulder = ['DOWN', 'DOWN', 'DOWN', 'DOWN', 'LEFT', 'LEFT', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'UP', 'UP', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'RIGHT', 'DOWN', 'DOWN', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'UP', 'UP', 'UP', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT']
sequence_to_exit_not_working = ['DOWN', 'DOWN', 'DOWN', 'DOWN', 'LEFT', 'LEFT', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'UP', 'UP', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'DOWN', 'RIGHT', 'DOWN', 'DOWN', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'UP', 'UP', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT'] #, 
sequence_to_exit = ['UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'LEFT', 'LEFT', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'LEFT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'LEFT', 'B', 'DOWN', 'B', 'RIGHT']
exited_sequence = ['RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'B', 'RIGHT', 'B', 'RIGHT', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP', 'UP']

###################
# SEAFOAM ISLANDS #
###################

# Seafoam 1F Left
STRENGTH_SOLUTIONS[(63, 14, 22, 18, 11, 192)] = [
    "UP",
    "UP",
    "UP",
    "UP",
    "UP",
    "UP",
    "UP",
    "UP",
    "UP",
    "UP",
    "UP",
    "UP",
    "UP",
    "UP",
    "UP",
    "UP",
    "RIGHT",
    "UP",
    "LEFT",
]
STRENGTH_SOLUTIONS[(63, 14, 22, 19, 10, 192)] = ["DOWN", "LEFT"] + STRENGTH_SOLUTIONS[
    (63, 14, 22, 18, 11, 192)
]
STRENGTH_SOLUTIONS[(63, 14, 22, 18, 9, 192)] = ["RIGHT", "DOWN"] + STRENGTH_SOLUTIONS[
    (63, 14, 22, 19, 10, 192)
]
STRENGTH_SOLUTIONS[(63, 14, 22, 17, 10, 192)] = ["UP", "RIGHT"] + STRENGTH_SOLUTIONS[
    (63, 14, 22, 18, 9, 192)
]

# Seafoam 1F right
STRENGTH_SOLUTIONS[(63, 11, 30, 26, 8, 192)] = [
    "UP",
    "RIGHT",
    "UP",
    "UP",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
]
STRENGTH_SOLUTIONS[(63, 11, 30, 27, 7, 192)] = ["DOWN", "LEFT"] + STRENGTH_SOLUTIONS[
    (63, 11, 30, 26, 8, 192)
]
STRENGTH_SOLUTIONS[(63, 11, 30, 26, 6, 192)] = ["RIGHT", "DOWN"] + STRENGTH_SOLUTIONS[
    (63, 11, 30, 27, 7, 192)
]
STRENGTH_SOLUTIONS[(63, 11, 30, 25, 7, 192)] = ["UP", "RIGHT"] + STRENGTH_SOLUTIONS[
    (63, 11, 30, 26, 6, 192)
]

# Seafoam B1 left

STRENGTH_SOLUTIONS[(63, 10, 21, 16, 6, 159)] = ["RIGHT"]
STRENGTH_SOLUTIONS[(63, 10, 21, 17, 5, 159)] = ["LEFT", "DOWN"] + STRENGTH_SOLUTIONS[
    (63, 10, 21, 16, 6, 159)
]
STRENGTH_SOLUTIONS[(63, 10, 21, 17, 7, 159)] = ["LEFT", "UP"] + STRENGTH_SOLUTIONS[
    (63, 10, 21, 16, 6, 159)
]

# Seafoam B1 right

STRENGTH_SOLUTIONS[(63, 10, 26, 21, 6, 159)] = ["RIGHT"]
STRENGTH_SOLUTIONS[(63, 10, 26, 22, 5, 159)] = ["LEFT", "DOWN"] + STRENGTH_SOLUTIONS[
    (63, 10, 26, 21, 6, 159)
]
STRENGTH_SOLUTIONS[(63, 10, 26, 22, 7, 159)] = ["LEFT", "UP"] + STRENGTH_SOLUTIONS[
    (63, 10, 26, 21, 6, 159)
]

# Seafoam B2 left

STRENGTH_SOLUTIONS[(63, 10, 22, 17, 6, 160)] = ["RIGHT"]
STRENGTH_SOLUTIONS[(63, 10, 22, 18, 5, 160)] = ["LEFT", "DOWN"] + STRENGTH_SOLUTIONS[
    (63, 10, 22, 17, 6, 160)
]
STRENGTH_SOLUTIONS[(63, 10, 22, 18, 7, 160)] = ["LEFT", "UP"] + STRENGTH_SOLUTIONS[
    (63, 10, 22, 17, 6, 160)
]

# Seafoam B2 right

STRENGTH_SOLUTIONS[(63, 10, 27, 24, 6, 160)] = ["LEFT"]
STRENGTH_SOLUTIONS[(63, 10, 27, 23, 7, 160)] = ["RIGHT", "UP"] + STRENGTH_SOLUTIONS[
    (63, 10, 27, 24, 6, 160)
]

# We skip seafoam b3 since that is for articuno
# TODO: Articuno

################
# VICTORY ROAD #
################

# 1F Switch 1
STRENGTH_SOLUTIONS[(63, 19, 9, 5, 14, 108)] = [
    "DOWN",
    "DOWN",
    "DOWN",
    "DOWN",
    "LEFT",
    "DOWN",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "DOWN",
    "RIGHT",
    "RIGHT",
    "UP",
    "UP",
    "UP",
    "UP",
    "UP",
    "UP",
    "LEFT",
    "UP",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "DOWN",
    "RIGHT",
    "UP",
    "UP",
    "UP",
    "LEFT",
    "LEFT",
    "UP",
    "UP",
    "UP",
    "UP",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "RIGHT",
    "UP",
    "RIGHT",
    "DOWN",
]



STRENGTH_SOLUTIONS[(63, 17, 21, 17, 11, 108)] = boulder_1_to_2
STRENGTH_SOLUTIONS[(63, 17, 21, 17, 12, 108)] = ['UP', 'UP'] + STRENGTH_SOLUTIONS[(63, 17, 21, 17, 11, 108)]

# picture_id, mapY, mapX, self.get_game_coords(): (6, 9, 11, (17, 11, 108))
# picture_id, mapY, mapX, self.get_game_coords(): (7, 6, 7, (17, 11, 108))
# picture_id, mapY, mapX, self.get_game_coords(): (61, 4, 15, (17, 11, 108))
# picture_id, mapY, mapX, self.get_game_coords(): (61, 6, 13, (17, 11, 108))
# picture_id, mapY, mapX, self.get_game_coords(): (63, 19, 9, (17, 11, 108))
# picture_id, mapY, mapX, self.get_game_coords(): (63, 6, 18, (17, 11, 108))
# picture_id, mapY, mapX, self.get_game_coords(): (63, 14, 6, (17, 11, 108))

# 2F Switch 1
STRENGTH_SOLUTIONS[(63, 18, 8, 5, 14, 194)] = [
    "LEFT",
    "LEFT",
    "UP",
    "LEFT",
    "DOWN",
    "DOWN",
    "DOWN",
    "DOWN",
    "DOWN",
    "DOWN",
    "RIGHT",
    "DOWN",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
]

STRENGTH_SOLUTIONS[(63, 18, 8, 4, 13, 194)] = ["RIGHT", "DOWN"] + STRENGTH_SOLUTIONS[
    (63, 18, 8, 5, 14, 194)
]
STRENGTH_SOLUTIONS[(63, 18, 8, 3, 14, 194)] = ["UP", "RIGHT"] + STRENGTH_SOLUTIONS[
    (63, 18, 8, 4, 13, 194)
]
STRENGTH_SOLUTIONS[(63, 18, 8, 4, 15, 194)] = ["LEFT", "UP"] + STRENGTH_SOLUTIONS[
    (63, 18, 8, 3, 14, 194)
]

STRENGTH_SOLUTIONS[(63, 18, 8, 4, 12, 194)] = ['DOWN']
STRENGTH_SOLUTIONS[(63, 18, 8, 3, 12, 194)] = ['RIGHT', 'DOWN']


STRENGTH_SOLUTIONS[(63, 20, 5, 2, 16, 194)] = boulder_2_to_3
STRENGTH_SOLUTIONS[(63, 20, 5, 3, 16, 194)] = ['LEFT'] + boulder_2_to_3


# picture_id, mapY, mapX, self.get_game_coords(): (14, 13, 16, (4, 12, 194))
# picture_id, mapY, mapX, self.get_game_coords(): (12, 17, 25, (4, 12, 194))
# picture_id, mapY, mapX, self.get_game_coords(): (7, 12, 23, (4, 12, 194))
# picture_id, mapY, mapX, self.get_game_coords(): (12, 6, 8, (4, 12, 194))
# picture_id, mapY, mapX, self.get_game_coords(): (12, 7, 30, (4, 12, 194))
# picture_id, mapY, mapX, self.get_game_coords(): (9, 9, 15, (4, 12, 194))
# picture_id, mapY, mapX, self.get_game_coords(): (61, 9, 31, (4, 12, 194))
# picture_id, mapY, mapX, self.get_game_coords(): (61, 13, 22, (4, 12, 194))
# picture_id, mapY, mapX, self.get_game_coords(): (61, 15, 13, (4, 12, 194))
# picture_id, mapY, mapX, self.get_game_coords(): (61, 4, 15, (4, 12, 194))
# picture_id, mapY, mapX, self.get_game_coords(): (63, 18, 8, (4, 12, 194))
# picture_id, mapY, mapX, self.get_game_coords(): (63, 9, 9, (4, 12, 194))
# picture_id, mapY, mapX, self.get_game_coords(): (63, 20, 27, (4, 12, 194))
# []
# (c, r, map_n) = (4, 12, 194)



# 3F Switch 3
STRENGTH_SOLUTIONS[(63, 19, 26, 22, 4, 198)] = [
    "UP",
    "UP",
    "UP",
    "RIGHT",
    "UP",
    "UP",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "UP",
    "LEFT",
    "DOWN",
    "RIGHT",
    "DOWN",
    "DOWN",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "LEFT",
    "UP",
    "UP",
    "LEFT",
    "DOWN",
    "DOWN",
    "DOWN",
    "DOWN",
    "DOWN",
    "DOWN",
    "DOWN",
    "DOWN",
    "DOWN",
    "LEFT",
    "DOWN",
    "RIGHT",
    "RIGHT",
]

STRENGTH_SOLUTIONS[(63, 19, 26, 23, 3, 198)] = ["DOWN", "LEFT"] + STRENGTH_SOLUTIONS[
    (63, 19, 26, 22, 4, 198)
]
STRENGTH_SOLUTIONS[(63, 19, 26, 22, 2, 198)] = ["RIGHT", "DOWN"] + STRENGTH_SOLUTIONS[
    (63, 19, 26, 23, 3, 198)
]
STRENGTH_SOLUTIONS[(63, 19, 26, 21, 3, 198)] = ["UP", "RIGHT"] + STRENGTH_SOLUTIONS[
    (63, 19, 26, 22, 2, 198)
]

STRENGTH_SOLUTIONS[(63, 19, 26, 23, 4, 198)] = ['LEFT']
STRENGTH_SOLUTIONS[(63, 19, 26, 2, 5, 198)] = boulder_3_to_4
STRENGTH_SOLUTIONS[(63, 10, 9, 5, 4, 194)] = ['DOWN', 'DOWN', 'DOWN']
STRENGTH_SOLUTIONS[(63, 9, 9, 5, 4, 194)] = ['DOWN', 'DOWN', 'DOWN']

STRENGTH_SOLUTIONS[(63, 11, 9, 5, 5, 194)] = ['DOWN', 'DOWN'] + active_strength_to_next_boulder + sequence_to_exit + exited_sequence



# 3F Boulder in hole
STRENGTH_SOLUTIONS[(63, 16, 17, 21, 15, 198)] = ["RIGHT", "RIGHT", "RIGHT"]
STRENGTH_SOLUTIONS[(63, 16, 17, 22, 16, 198)] = ["LEFT", "UP"] + STRENGTH_SOLUTIONS[
    (63, 16, 17, 21, 15, 198)
]
STRENGTH_SOLUTIONS[(63, 16, 17, 22, 14, 198)] = ["LEFT", "DOWN"] + STRENGTH_SOLUTIONS[
    (63, 16, 17, 21, 15, 198)
]


# # 2F final switch
# STRENGTH_SOLUTIONS[(63, 20, 27, 24, 16, 194)] = [
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
#     "LEFT",
# ]

# STRENGTH_SOLUTIONS[(63, 20, 27, 23, 17, 194)] = ["RIGHT", "UP"] + STRENGTH_SOLUTIONS[
#     (63, 20, 27, 24, 16, 194)
# ]
# STRENGTH_SOLUTIONS[(63, 20, 27, 22, 16, 194)] = ["DOWN", "RIGHT"] + STRENGTH_SOLUTIONS[
#     (63, 20, 27, 23, 17, 194)
# ]

# picture_id, mapY, mapX, self.get_game_coords(): (14, 13, 16, (21, 16, 194))
# picture_id, mapY, mapX, self.get_game_coords(): (12, 17, 23, (21, 16, 194))
# picture_id, mapY, mapX, self.get_game_coords(): (7, 12, 23, (21, 16, 194))
# picture_id, mapY, mapX, self.get_game_coords(): (12, 6, 8, (21, 16, 194))
# picture_id, mapY, mapX, self.get_game_coords(): (12, 7, 30, (21, 16, 194))
# picture_id, mapY, mapX, self.get_game_coords(): (9, 9, 15, (21, 16, 194))
# picture_id, mapY, mapX, self.get_game_coords(): (61, 9, 31, (21, 16, 194))
# picture_id, mapY, mapX, self.get_game_coords(): (61, 13, 22, (21, 16, 194))
# picture_id, mapY, mapX, self.get_game_coords(): (61, 15, 13, (21, 16, 194))
# picture_id, mapY, mapX, self.get_game_coords(): (61, 4, 15, (21, 16, 194))
# picture_id, mapY, mapX, self.get_game_coords(): (63, 20, 5, (21, 16, 194))
# picture_id, mapY, mapX, self.get_game_coords(): (63, 11, 9, (21, 16, 194))
# picture_id, mapY, mapX, self.get_game_coords(): (63, 20, 27, (21, 16, 194))
# []
# (c, r, map_n) = (21, 16, 194)


STRENGTH_SOLUTIONS[(63, 19, 9, 4, 15, 108)] = ["UP", "RIGHT"] + STRENGTH_SOLUTIONS[
    (63, 19, 9, 5, 14, 108)] # + ['B'] +  STRENGTH_SOLUTIONS[(63, 17, 21, 17, 11, 108)] + ['B'] + STRENGTH_SOLUTIONS[(63, 18, 8, 5, 14, 194)] + ['B'] + STRENGTH_SOLUTIONS[(63, 20, 5, 2, 16, 194)] + ['B'] + STRENGTH_SOLUTIONS[(63, 19, 26, 22, 4, 198)] + ['B'] + STRENGTH_SOLUTIONS[(63, 19, 26, 2, 5, 198)] + ['B']

# STRENGTH_SOLUTIONS[(63, 19, 9, 5, 16, 108)] = ["LEFT", "UP"] + STRENGTH_SOLUTIONS[
#     (63, 19, 9, 4, 15, 108)] + ['B'] + STRENGTH_SOLUTIONS[(63, 17, 21, 17, 11, 108)] + ['B'] + STRENGTH_SOLUTIONS[(63, 18, 8, 5, 14, 194)] + ['B'] + STRENGTH_SOLUTIONS[(63, 20, 5, 2, 16, 194)] + ['B'] + STRENGTH_SOLUTIONS[(63, 19, 26, 22, 4, 198)] + ['B'] + STRENGTH_SOLUTIONS[(63, 19, 26, 2, 5, 198)] + ['B']

# STRENGTH_SOLUTIONS[(63, 14, 6, 17, 11, 108)] = ["B"]

STRENGTH_SOLUTIONS[(63, 18, 8, 3, 12, 194)] = ["B"]
# STRENGTH_SOLUTIONS[(63, 18, 8, 4, 13, 194)] = ["B"]
STRENGTH_SOLUTIONS[(63, 20, 27, 2, 16, 194)] = ["B"]
STRENGTH_SOLUTIONS[(63, 19, 26, 23, 4, 198)] = ["B"]

# STRENGTH_SOLUTIONS[(63, 20, 27, 5, 4, 194)] = ["B"]

