from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))

with open("data.txt") as f:
    data = f.read().splitlines()

for y, row in enumerate(data):
    for x, char in enumerate(row):
        if char == "S":
            heap = [(0, x, y, 1)]

visited = set()
while heap:
    score, x, y, direction = heappop(heap)

    if (x, y) in visited:
        continue
    visited.add((x, y))
    
    if data[y][x] == "E":
        print(score)
        break

    for newDir, (dx, dy) in enumerate(DIRECTIONS):
        if not (0 <= dx+x < len(data[0]) and 0 <= dy+y < len(data)):
            continue

        if data[dy+y][dx+x] == "#":
            continue

        heappush(heap, (score + (1 if newDir == direction else 1001), dx+x, dy+y, newDir))