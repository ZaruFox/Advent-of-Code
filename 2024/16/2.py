from collections import deque, defaultdict, Counter
import functools
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
from sys import setrecursionlimit
from matplotlib.pylab import permutation
import numpy

DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))

with open("data.txt") as f:
    data = f.read().splitlines()

def bfs():
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == "S":
                startPos = (x, y, DIRECTIONS.index((1, 0)))
                
    heap = [(0, *startPos)] 
    visited = defaultdict(lambda: math.inf)
    prev = defaultdict(set)
    visited[startPos] = 0

    while heap:
        score, x, y, direction = heappop(heap)

        if visited[(x, y, direction)] != score:
            continue

        dx, dy = DIRECTIONS[direction]
        for newLocation in ((dx+x, dy+y, direction), (x, y, (direction-1)%4), (x, y, (direction+1)%4)):
            if not (0 <= newLocation[0] < len(data[0]) and 0 <= newLocation[1] < len(data)):
                continue

            if data[newLocation[1]][newLocation[0]] == "#":
                continue

            newScore = score + (1 if newLocation[2] == direction else 1000)

            if visited[newLocation] < newScore:
                continue

            if newScore < visited[newLocation]:
                visited[newLocation] = newScore
                prev[newLocation] = set()
                heappush(heap, (newScore, *newLocation))

            prev[newLocation].add((x, y, direction))
    
    return prev

def getValidSpots(prev, x, y, dir):
    res = {(x, y)}
    for prevPos in prev[(x, y, dir)]:
        res |= getValidSpots(prev, *prevPos)

    return res

print(len(getValidSpots(bfs(), 139, 1, 2)))

