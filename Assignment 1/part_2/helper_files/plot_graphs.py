# File just to get the graph plots and analysis for the different methods
import os

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from io_helper import get_project_path

path = get_project_path()
vresults_path = os.path.join(path, 'part_2', 'results', 'Value Iteration')
presults_path = os.path.join(path, 'part_2', 'results', 'Policy Iteration')

try:
    os.makedirs(vresults_path)
    os.makedirs(presults_path)
except os.error:
    pass
rfile_vi = os.path.join(vresults_path, 'VI vs Utility [Part 2 Complex Maze].png')
rfile_pi = os.path.join(presults_path, 'PI vs Utility [Part 2 Complex Maze].png')
value_headers = ['State', 'Iteration', 'Utility']
# Policy has action
policy_headers = ['State', 'Iteration', 'Action', 'Utility']

"""
just change the name in the csv write/read
Value Iteration (Part 2).csv
Policy Iteration (Part 2).csv
"""

value_df = pd.read_csv(os.path.join(vresults_path, 'Value Iteration (Part 2).csv'), names = value_headers, index_col='State')
policy_df = pd.read_csv(os.path.join(presults_path, 'Policy Iteration (Part 2).csv'), names = policy_headers, index_col='State')


def analysis(vorp,pos):
    if vorp == 0:
        value_state_df = value_df.loc[pos]
        return value_state_df
    else:
        policy_state_df = policy_df.loc[pos]
        return policy_state_df

# change the values to 9 and 9 for the 10x10 complicated maze
colsize= 5
rowsize= 5
positions =[]

for x in range(0,colsize+1):
    for y in range(0,rowsize+1):
        stringcall = ",".join(str(x)+str(y))
        stringcall="("+stringcall +")"
        positions.append(stringcall)
        stringcall =""

figure(figsize=(16, 8))

for x in positions:
    value_state_df = analysis(0,x)
    plt.plot(value_state_df['Iteration'], value_state_df['Utility'], label=x)
plt.title("VI vs Utility [Part 1: Complex Maze]")
plt.xlabel("Iterations")
plt.ylabel("Utility Values")
plt.legend(loc=2, prop={'size': 6})
plt.savefig(rfile_vi)
plt.show()


figure(figsize=(16, 8))
for x in positions:
    policy_state_df = analysis(1,x)
    plt.plot(policy_state_df['Iteration'], policy_state_df['Utility'], label=x)
plt.title("PI vs Utility [Part 2: Complex Maze]")
plt.xlabel("Iterations")
plt.ylabel("Utility Values")
plt.legend(loc=2, prop={'size': 6})
plt.savefig(rfile_pi)
plt.show()