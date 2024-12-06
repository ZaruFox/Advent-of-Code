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

directions = ((0,-1), (1,0), (0,1), (-1, 0))
curDir = 0
visited = set()

while 0 <= curY < len(data) and 0 <= curX < len(data[0]):
    dx, dy = directions[curDir]
    visited.add((curX, curY))
    
    if (0 <= curY+dy < len(data) and 0 <= curX+dx < len(data[0])) and data[curY+dy][curX+dx] == "#":
            curDir = (curDir+1)%4
    else:
        curX += dx
        curY += dy
    
print(len(visited))

    
    