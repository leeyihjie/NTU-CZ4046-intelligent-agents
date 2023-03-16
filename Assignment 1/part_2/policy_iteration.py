import csv
import copy
import os
import random

from .helper_files.appdata import *
from .helper_files.set_decimel import truncate
from .helper_files.io_helper import get_project_path

path = get_project_path()
results_path = os.path.join(path, 'part_2', 'results', 'Policy Iteration')
try:
    os.makedirs(results_path)
except os.error:
    pass
# Creating Grid World
# Initialise reward values as 0

def initialise_env():
    environment = [[0] * NUM_COLS for i in range(NUM_ROWS)]

    # # Input positive and negative reward values into environment
    # for coord in POSITIVE_REWARD_GRIDS:
    #     environment[coord[0]][coord[1]] = 1
    # for coord in NEGATIVE_REWARD_GRIDS:
    #     environment[coord[0]][coord[1]] = -1

    # fixed_action = 'UP'  # ('UP', 'DOWN', 'LEFT', 'RIGHT')
    policy = [[random.choice(ACTIONS)] * NUM_COLS for i in range(NUM_ROWS)] # Random Policy for each cell

    return environment, policy


def print_environment(env):
    # Show outcome of iterations
    display = ""
    display += '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓' + ' Grid World Matrix ' + '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\n'
    display += "+————————+————————+————————+————————+————————+————————+————————+————————+————————+————————+\n"
    for row in range(NUM_ROWS):
        display += "|"
        for col in range(NUM_COLS):
            if (row, col) in WALL_REWARD_GRIDS:
                val = " W " + str(env[row][col])
                display += "" + val[:7].ljust(6) + "  |"
            elif (row, col) in POSITIVE_REWARD_GRIDS:
                val = "G " + str(env[row][col])
                display += "" + val[:7].ljust(7) + " |"
            elif (row, col) in NEGATIVE_REWARD_GRIDS:
                val = "B " + str(env[row][col])
                display += "" + val[:7].ljust(7) + " |"
            else:
                val = str(env[row][col])
                display += "  " + val[:5].ljust(5) + " |"
                # if env[row][col] == 0:
                #     val = ''
            # display += " " + val[:5].ljust(5) + " |"
        display += "\n"
        display += "+————————+————————+————————+————————+————————+————————+————————+————————+————————+————————+\n"
    print(display)


# Prints out the given policy (recommended action at each state)
def print_policy(policy):
    display = ""
    display += '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓' + ' Optimal Policy Matrix ' + '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\n'
    display += "+————————+————————+————————+————————+————————+————————+————————+————————+————————+————————+\n"
    for row in range(NUM_ROWS):
        display += "|"
        for col in range(NUM_COLS):
            if policy[row][col] == 'UP':
                arrow = 0
            elif policy[row][col] == 'DOWN':
                arrow = 1
            elif policy[row][col] == 'LEFT':
                arrow = 2
            elif policy[row][col] == 'RIGHT':
                arrow = 3
            if (row, col) in WALL_REWARD_GRIDS:
                val = "W"
            elif START_POINT != None and (row, col) == START_POINT:
                val = "SP" + " (" + ["↑", "↓", "←", "→"][arrow] + ")"
            elif (row, col) in POSITIVE_REWARD_GRIDS:
                val = "G" + " (" + ["↑", "↓", "←", "→"][arrow] + ")"
            elif (row, col) in NEGATIVE_REWARD_GRIDS:
                val = "B" + " (" + ["↑", "↓", "←", "→"][arrow] + ")"
            else:
                val = ["↑", "↓", "←", "→"][arrow]
            display += " " + val[:6].ljust(6) + " |"
        display += "\n"
        display += "+————————+————————+————————+————————+————————+————————+————————+————————+————————+————————+\n"
    print(display)

# returns utility value of next state given current state (row, col) and action taken
def next_state_utility(env, row, col, action):
    if (row, col) in WALL_REWARD_GRIDS:
        return env[row][col]
    elif action == 'UP':
        move_up_row, move_up_col = ACTIONS_LIST['UP']
        new_row = row + move_up_row
        new_col = col + move_up_col

        # Check if action is legal/has legal next state
        if new_row < 0 or new_row >= NUM_ROWS or new_col < 0 or new_col >= NUM_COLS or (
                new_row, new_col) in WALL_REWARD_GRIDS:
            return env[row][col]
        else:
            return env[new_row][new_col]
    elif action == 'DOWN':
        move_down_row, move_down_col = ACTIONS_LIST['DOWN']
        new_row = row + move_down_row
        new_col = col + move_down_col

        # Check if action is legal/has legal next state
        if new_row < 0 or new_row >= NUM_ROWS or new_col < 0 or new_col >= NUM_COLS or (
                new_row, new_col) in WALL_REWARD_GRIDS:
            return env[row][col]
        else:
            return env[new_row][new_col]
    elif action == 'LEFT':
        move_left_row, move_left_col = ACTIONS_LIST['LEFT']
        new_row = row + move_left_row
        new_col = col + move_left_col

        # Check if action is legal/has legal next state
        if new_row < 0 or new_row >= NUM_ROWS or new_col < 0 or new_col >= NUM_COLS or (
                new_row, new_col) in WALL_REWARD_GRIDS:
            return env[row][col]
        else:
            return env[new_row][new_col]
    elif action == 'RIGHT':
        move_right_row, move_right_col = ACTIONS_LIST['RIGHT']
        new_row = row + move_right_row
        new_col = col + move_right_col

        # Check if action is legal/has legal next state
        if new_row < 0 or new_row >= NUM_ROWS or new_col < 0 or new_col >= NUM_COLS or (
                new_row, new_col) in WALL_REWARD_GRIDS:
            return env[row][col]
        else:
            return env[new_row][new_col]

# Returns expected utility of taking action 'a' in state 's'
def expected_utility(env, row, col, action):
    exp_utility = 0
    if action == 'UP':
        exp_utility += 0.1 * next_state_utility(env, row, col, 'LEFT')
        exp_utility += 0.8 * next_state_utility(env, row, col, 'UP')
        exp_utility += 0.1 * next_state_utility(env, row, col, 'RIGHT')
    elif action == 'DOWN':
        exp_utility += 0.1 * next_state_utility(env, row, col, 'LEFT')
        exp_utility += 0.8 * next_state_utility(env, row, col, 'DOWN')
        exp_utility += 0.1 * next_state_utility(env, row, col, 'RIGHT')
    elif action == 'LEFT':
        exp_utility += 0.1 * next_state_utility(env, row, col, 'UP')
        exp_utility += 0.8 * next_state_utility(env, row, col, 'LEFT')
        exp_utility += 0.1 * next_state_utility(env, row, col, 'DOWN')
    elif action == 'RIGHT':
        exp_utility += 0.1 * next_state_utility(env, row, col, 'UP')
        exp_utility += 0.8 * next_state_utility(env, row, col, 'RIGHT')
        exp_utility += 0.1 * next_state_utility(env, row, col, 'DOWN')
    #print('expected_utility: ', (row, col), action, exp_utility)
    return exp_utility

# Implementation of modified bellman equation
def bellman_equation(env, row, col, action):
    if (row, col) in POSITIVE_REWARD_GRIDS:
        reward = 1
    elif (row, col) in NEGATIVE_REWARD_GRIDS:
        reward = -1
    elif (row, col) in WALL_REWARD_GRIDS:
        reward = 0
    else:
        reward = -0.04

    utility = expected_utility(env, row, col, action)

    return reward + (DISCOUNT_FACTOR * utility)

# Performs evaluation of the current policy
def policy_evaluation(policy, env, iteration):
    while True:
        next_env = copy.deepcopy(env)
        error = 0
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                max_utility = bellman_equation(env, row, col, policy[row][col])
                # print("actual max util: ", max_utility, "actual best action: ", best_action)
                next_env[row][col] = max_utility
                error = max(error, abs(next_env[row][col] - env[row][col]))

        env = next_env
        if error < SMALL_ENOUGH:
            break

    rfile = os.path.join(results_path, 'Policy Iteration (Part 2).csv')
    with open(rfile, 'a', newline='') as file:
        writer = csv.writer(file)
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                writer.writerow([f"({row},{col})", iteration, policy[row][col], truncate(env[row][col], 3)])

    print_environment(env)
    return env

def policy_iteration(policy, env):
    iteration = 1
    while True:
        environment = policy_evaluation(policy, env, iteration)
        is_changed = False
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                best_action = None
                max_utility = -float("inf")
                for action in ACTIONS:
                    utility = bellman_equation(environment, row, col, action)
                    if utility > max_utility:
                        best_action = action
                        max_utility = utility

                if max_utility > bellman_equation(environment, row, col, policy[row][col]):
                    policy[row][col] = best_action
                    is_changed = True

        if is_changed:
            print(f"Iteration {iteration}")
            print_policy(policy)

        if is_changed == False:
            break

        iteration += 1

    return policy


# write data to csv
def open_file():
    rfile = os.path.join(results_path, 'Policy Iteration (Part 2).csv')
    with open(rfile, 'w', newline='') as file:
        writer = csv.writer(file)
