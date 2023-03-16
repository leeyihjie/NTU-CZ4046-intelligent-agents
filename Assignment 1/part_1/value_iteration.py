import copy
import csv
import os

from .helper_files.appdata import *
from .helper_files.set_decimel import truncate
from .helper_files.io_helper import get_project_path

path = get_project_path()
results_path = os.path.join(path, 'part_1', 'results', 'Value Iteration')
try:
    os.makedirs(results_path)
except os.error:
    pass

# Creating Grid World
# Initialise reward values as 0
def initialise_env():
    environment = [[0] * NUM_COLS for i in range(NUM_ROWS)]
    return environment


def print_environment(env):
    # Show outcome of iterations
    display = ""
    display += '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓' + ' Grid World Matrix ' + '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\n'
    display += "+————————+————————+————————+————————+————————+————————+\n"
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
        display += "+————————+————————+————————+————————+————————+————————+\n"
    print(display)


# Implementation of Ui[s′]
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


# Implementation of ∑s′P(s′|s, a)U[s′]
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
    return exp_utility


# Implementation of full bellman equation: Ui+1[s] ← R(s) + γ max a∈A(s) ∑s′P(s′|s, a)Ui[s′]
def bellman_equation(env, row, col):
    if (row, col) in POSITIVE_REWARD_GRIDS:
        reward = 1
    elif (row, col) in NEGATIVE_REWARD_GRIDS:
        reward = -1
    elif (row, col) in WALL_REWARD_GRIDS:
        reward = 0
    else:
        reward = -0.04

    max_utility = -float("inf")
    best_action = None
    for action in ACTIONS:
        utility = expected_utility(env, row, col, action)
        if utility > max_utility:
            max_utility = utility
            best_action = action
            #print("max util: ", max_utility, "best action: ", best_action)
            #print("max bellmon: ", reward + (DISCOUNT_FACTOR * max_utility), "best action: ", best_action)


    return (reward + (DISCOUNT_FACTOR * max_utility)), best_action


def value_iteration(env):
    rfile = os.path.join(results_path, 'Value Iteration (Part 1).csv')
    with open(rfile, 'a', newline='') as file:
        writer = csv.writer(file)
        # open csv to store data there, easier to refer
        # Initial values are all 0
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                writer.writerow([f"({row},{col})", 0, 0])
        iteration = 1
        while True:
            print(f"Iteration Number: {iteration}")
            next_env = copy.deepcopy(env)
            error = 0
            for row in range(NUM_ROWS):
                for col in range(NUM_COLS):
                    max_utility, best_action = bellman_equation(env, row, col)
                    #print("actual max util: ", max_utility, "actual best action: ", best_action)
                    next_env[row][col] = max_utility
                    error = max(error, abs(next_env[row][col] - env[row][col]))
                    writer.writerow([f"({row},{col})", iteration, truncate(next_env[row][col], 3)])

            env = next_env
            # Return new iteration count
            print_environment(env)
            if error < SMALL_ENOUGH * (1 - DISCOUNT_FACTOR) / DISCOUNT_FACTOR:
                break
            iteration += 1
        return env


def get_optimal_policy(env):
    policy = [[-1] * NUM_COLS for i in range(NUM_ROWS)]

    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            max_utility = -float("inf")
            best_action = None
            for action in ACTIONS:
                exp_utility = expected_utility(env, row, col, action)
                if exp_utility > max_utility:
                    max_utility = exp_utility
                    best_action = action
            policy[row][col] = best_action
    # Return optimal policy for policy extraction step
    return policy


def print_policy(policy):
    display = ""
    display += '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓' + ' Optimal Policy Matrix ' + '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\n'
    display += "+————————+————————+————————+————————+————————+————————+\n"
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
        display += "+————————+————————+————————+————————+————————+————————+\n"
    print(display)

def open_file():
    rfile = os.path.join(results_path, 'Value Iteration (Part 1).csv')
    with open(rfile, 'w', newline='') as file:
        writer = csv.writer(file)