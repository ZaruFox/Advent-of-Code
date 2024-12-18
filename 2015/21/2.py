from collections import deque, defaultdict, Counter
import functools
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

bossStats = []
for line in data:
    _, stat = line.split(": ")
    bossStats.append(int(stat))

weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
armor = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
rings = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]

loadouts = [[x] for x in weapons]
loadouts += [a+[b] for a, b in itertools.product(loadouts, armor)]
loadouts += [a+[b] for a, b in itertools.product(loadouts, rings)]
loadouts += [a+[b] for a, b in itertools.product(loadouts, rings) if a[-1] != b]

loadouts = [[sum(x[j][i] for j in range(len(x))) for i in range(3)] for x in loadouts]
loadouts.sort(reverse=True)

for cost, damage, armor in loadouts:
    playerHealth = 100
    bossHealth = bossStats[0]

    while True:
        bossHealth -= damage - bossStats[2]
        
        if bossHealth <= 0:
            break

        playerHealth -= bossStats[1] - armor

        if playerHealth <= 0:
            print(cost)
            exit()