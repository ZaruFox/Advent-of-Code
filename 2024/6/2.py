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

def checkLoop(curX, curY, newX, newY): 
    directions = ((0,-1), (1,0), (0,1), (-1, 0))
    curDir = 0
    visited = set()
    
    while 0 <= curY < len(data) and 0 <= curX < len(data[0]):
        dx, dy = directions[curDir]
        if (curX, curY, curDir) in visited:
            return True
        visited.add((curX, curY, curDir))
    
        if (0 <= curY+dy < len(data) and 0 <= curX+dx < len(data[0])) and (data[curY+dy][curX+dx] == "#" or (curX+dx, curY+dy) == (newX, newY)):
            curDir = (curDir+1)%4
        else:
            curX += dx
            curY += dy

    return False
res = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "." and checkLoop(curX, curY, x, y):
            res += 1
print(res)