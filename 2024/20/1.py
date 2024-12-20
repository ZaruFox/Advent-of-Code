from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

def startToEnd(walls, startPos, endPos, n, m):
    queue = deque([(startPos, 0)])
    visited = set()

    while queue:
        pos, cost = queue.popleft()

        if pos in visited:
            continue
        visited.add(pos)

        if pos == endPos:
            return cost

        x, y = pos
        for newX, newY in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
            if not (0 <= newX < m and 0 <= newY < n) or (x, y) in walls:
                continue

            queue.append(((newX, newY), cost+1))

    return -1

def bfs(walls, startPos, n, m):
    queue = deque([(startPos, 0)])
    visited = {}

    while queue:
        pos, cost = queue.popleft()

        if pos in visited:
            continue
        visited[pos] = cost

        x, y = pos
        for newX, newY in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
            if not (0 <= newX < m and 0 <= newY < n) or (x, y) in walls:
                continue

            queue.append(((newX, newY), cost+1))

    return visited

def getValidCheats(walls, startPos, n, m):
    queue = deque([(startPos, 0)])
    visited = {}

    while queue:
        pos, cost = queue.popleft()

        if pos in visited:
            continue
        visited[pos] = cost

        x, y = pos
        for newX, newY in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
            if not (0 <= newX < m and 0 <= newY < n) or cost+1 > 2:
                continue

            queue.append(((newX, newY), cost+1))

    return {pos: cost for pos, cost in visited.items() if pos not in walls}

n = len(data)
m = len(data[0])

walls = set()
for y, row in enumerate(data):
    for x, char in enumerate(row):
        if char == "S":
            startPos = (x, y)

        elif char == "E":
            endPos = (x, y)

        elif char == "#":
            walls.add((x, y))

base = startToEnd(walls, startPos, endPos, n, m)
distFromStart = bfs(walls, startPos, n, m)
distFromEnd = bfs(walls, endPos, n, m)
res = 0

for y in range(n):
    for x in range(m):
        if (x, y) in walls:
            continue

        for endPoint, cost in getValidCheats(walls, (x, y), n, m).items():
            dist = distFromStart[(x, y)] + cost + distFromEnd[endPoint]

            if base - dist >= 100:
                res += 1

print(res)