from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = [[int(x) for x in row] for row in f.read().splitlines()]

startingPoints = []
for y, row in enumerate(data):
    for x, char in enumerate(row):
        if char == 0:
            startingPoints.append((x,y))

def bfs(startX, startY):
    stack = deque([(startX, startY)])
    visited = set()
    res = 0

    while stack:
        x, y = stack.popleft()

        if data[y][x] == 9:
            res += 1
            continue
        
        for newX, newY in ((x-1, y), (x+1, y), (x, y+1), (x, y-1)):
            if not (0 <= newX < len(data[0]) and 0 <= newY < len(data)) or data[y][x] + 1 != data[newY][newX]:
                continue

            stack.append((newX, newY))

    return res

print(sum(bfs(*coords) for coords in startingPoints))
