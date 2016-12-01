__author__ = "Sriram Jayaraman"

import numpy as np

positions = ['GK', 'LCD', 'RCD', 'LB', 'RB', 'LCM', 'RCM', 'LW', 'RW', 'LS', 'RS']
print("Enter the heights of the various players(The first Eleven): ")
heights = [int(x) for x in input().split()]
if len(heights) != len(positions):
    print("Insufficient Data")
    exit(0)
np_positions=np.array(positions)
np_heights=np.array(heights)
gk_heights=np_heights[np_positions=='GK']
other_heights=np_heights[np_positions!='GK']
print("Median height of goalkeepers: " + str(np.median(gk_heights)))
print("Median height of other players: " + str(np.median(other_heights)))