"""
Values of variables, constants and configurations are defined here
Legend:
'W' = wall = 0 reward
"G" = green = +1 reward
"B" = brown = -1 reward
" " = white square = -0.04 reward
"""

'''
GRID = [
    ['G', 'W', 'G', ' ', ' ', 'G'],
    [' ', 'B', ' ', 'G', 'W', 'B'],
    [' ', ' ', 'B', ' ', 'G', ' '],
    [' ', ' ', ' ', 'B', ' ', 'G'],
    [' ', 'W', 'W', 'W', 'B', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ']
]
'''

START_POINT = (3, 2)  # 4th row, 3rd column

POSITIVE_REWARD_GRIDS = [(0, 0), (0, 2), (0, 5), (1, 3), (2, 4), (3, 5)]  # 'G' cells
NEGATIVE_REWARD_GRIDS = [(1, 1), (1, 5), (2, 2), (3, 3), (4, 4)]  # 'B' cells
WALL_REWARD_GRIDS = [(0, 1), (1, 4), (4, 1), (4, 2), (4, 3)]  # 'W' cells
NUM_ROWS = 6
NUM_COLS = 6
DISCOUNT_FACTOR = 0.99
R_MAX = 1.00
C = 0.10
EPSILON = C * R_MAX
SMALL_ENOUGH = EPSILON * (1 - DISCOUNT_FACTOR) / DISCOUNT_FACTOR
#SMALL_ENOUGH = 10**(-2)

ACTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT']

ACTIONS_LIST = {
    'UP': (-1, 0),
    'DOWN': (1, 0),
    'LEFT': (0, -1),
    'RIGHT': (0, 1)
}

