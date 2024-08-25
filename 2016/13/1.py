from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

@cache
def isWall(x, y, favouriteNumber):
    tmp = x*x + 3*x + 2*x*y + y + y*y + favouriteNumber
    return f"{tmp:b}".count("1") % 2 == 1

with open("data.txt") as f:
    favouriteNumber = int(f.readline().strip())

queue = deque([(1, 1, 0)])
visited = {(1, 1)}

while queue:
    x, y, cost = queue.popleft()

    for nextX, nextY in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
        if (nextX, nextY) == (31, 39):
            print(cost+1)
            exit()

        if isWall(nextX, nextY, favouriteNumber) or (nextX, nextY) in visited or nextX < 0 or nextY < 0:
            continue
        visited.add((nextX, nextY))

        queue.append((nextX, nextY, cost+1))
