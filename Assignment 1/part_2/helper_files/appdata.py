"""
Values of variables, constants and configurations are defined here
Legend:
'W' = wall = 0 reward
"G" = green = +1 reward
"B" = brown = -1 reward
" " = white square = -0.04 reward
"""

'''
10*10 maze 
GRID = [
      0    1    2    3    4    5    6    7    8    9
0   ['B', 'W', 'G', ' ', ' ', 'G', ' ', ' ', 'W', 'G'],
1   [' ', 'B', ' ', 'B', 'W', ' ', ' ', ' ', 'W', 'G'],
2   [' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', ' ', 'G'],
3   [' ', ' ', ' ', 'B', ' ', 'G', 'G', 'B', 'B', 'B'],
4   [' ', 'W', 'W', 'W', 'W', 'B', 'W', 'W', 'W', 'W'],
5   [' ', ' ', ' ', ' ', ' ', ' ', 'G', ' ', 'G', 'B'],
6   ['G', 'W', 'G', ' ', ' ', ' ', 'G', ' ', 'G', 'B'],
7   [' ', 'B', 'W', 'W', 'W', 'W', 'W', ' ', 'W', 'W'],
8   [' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', 'W', 'B'],
9   ['S', ' ', ' ', ' ', ' ', ' ', ' ', 'G', 'G', 'B']
]
'''

START_POINT = (9, 0)  # 10th row, 1st column

POSITIVE_REWARD_GRIDS = [(0, 2), (0, 5), (0, 9),
                         (1, 9),
                         (2, 9),
                         (3, 5), (3, 6),
                         (5, 6), (5, 8),
                         (6, 0), (6, 2), (6, 6), (6, 8),
                         (9, 7), (9, 8)]  # 'G' cells
NEGATIVE_REWARD_GRIDS = [(0, 0),
                         (1, 1), (1, 3),
                         (2, 4),
                         (3, 3), (3, 7), (3, 8), (3, 9),
                         (4, 5),
                         (5, 9),
                         (6, 9),
                         (7, 1),
                         (8, 4), (8, 9),
                         (9, 9)]  # 'B' cells
WALL_REWARD_GRIDS = [(0, 1), (0, 8),
                     (1, 4), (1, 8),
                     (2, 2),
                     (4, 1), (4, 2), (4, 3), (4, 4), (4, 6), (4, 7), (4, 8), (4, 9),
                     (6, 1),
                     (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 8), (7, 9),
                     (8, 8)]  # 'W' cells
NUM_ROWS = 10
NUM_COLS = 10
DISCOUNT_FACTOR = 0.999
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

