from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math

with open("data.txt") as f:
    data = f.read().splitlines()

for y, row in enumerate(data):
    for x, char in enumerate(row):
        if char == "^":
            curX = x
            curY = y

DIRECTIONS = ((0,-1), (1,0), (0,1), (-1, 0))
n, m = len(data), len(data[0])
curDir = 0
visited = set()

while True:
    dx, dy = DIRECTIONS[curDir]
    visited.add((curX, curY))
    
    if not (0 <= curY+dy < n and 0 <= curX+dx < m):
         break
    
    elif data[curY+dy][curX+dx] == "#":
            curDir = (curDir + 1) % 4

    else:
        curX += dx
        curY += dy
    
print(len(visited))

    
    