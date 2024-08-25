from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

with open("data.txt") as f:
    grid = f.read().splitlines()

curPos = (len(grid)//2, len(grid)//2)
curDirection = 0
res = 0
infected = set()
weakened = set()
flagged = set()

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "#":
            infected.add((x, y))

for _ in range(10000000):
    if curPos in infected:
        curDirection += 1
        curDirection %= 4
        infected.remove(curPos)
        flagged.add(curPos)
        
    elif curPos in weakened:
        res += 1
        weakened.remove(curPos)
        infected.add(curPos)
    
    elif curPos in flagged:
        curDirection += 2
        curDirection %= 4
        flagged.remove(curPos)

    else:
        curDirection -= 1
        curDirection %= 4
        weakened.add(curPos)

    curPos = (curPos[0] + DIRECTIONS[curDirection][0], curPos[1] + DIRECTIONS[curDirection][1])

print(res)