from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math

DIRECTIONS = ((0,-1), (1,0), (0,1), (-1, 0))

def checkLoop(curX, curY, newX, newY): 
    curDir = 0
    visited = set()
    
    while True:
        dx, dy = DIRECTIONS[curDir]
        if (curX, curY, curDir) in visited:
            return True
        visited.add((curX, curY, curDir))

        if not (0 <= curY+dy < len(data) and 0 <= curX+dx < len(data[0])):
            return False
    
        elif (data[curY+dy][curX+dx] == "#" or (curX+dx, curY+dy) == (newX, newY)):
            curDir = (curDir+1)%4

        else:
            curX += dx
            curY += dy


with open("data.txt") as f:
    data = f.read().splitlines()

for y, row in enumerate(data):
    for x, char in enumerate(row):
        if char == "^":
            startX = x
            startY = y

n, m = len(data), len(data[0])
curDir = 0
visited = set()
curX, curY = startX, startY

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

res = 0
for x, y in visited:
    if checkLoop(startX, startY, x, y):
        res += 1
print(res)