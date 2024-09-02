from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

def bfsMaze(n, grid, startX, startY):
    res = [-1] * n
    queue = deque([(startX, startY, 0)])
    visited = set()

    while queue:
        x, y, cost = queue.popleft()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        if grid[y][x].isdigit():
            res[int(grid[y][x])] = cost

        for newX, newY in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
            if grid[newY][newX] == "#":
                continue

            queue.append((newX, newY, cost+1))

    return res

def dfs(n, adjGraph, cur, visited):
    if len(visited) == n:
        return adjGraph[cur][0]

    minCost = math.inf

    for nextNode, cost in enumerate(adjGraph[cur]):
        if nextNode == cur or nextNode in visited:
            continue

        visited.add(nextNode)
        minCost = min(dfs(n, adjGraph, nextNode, visited) + cost, minCost)
        visited.discard(nextNode)

    return minCost

with open("data.txt") as f:
    data = f.read().splitlines()

n = 8
adjGraph = [None] * n

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x].isdigit():
            adjGraph[int(data[y][x])] = bfsMaze(n, data, x, y)

print(dfs(n, adjGraph, 0, {0}))