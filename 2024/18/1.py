from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

n = 71
walls = []
for line in data:
    walls.append(tuple(map(int, line.split(","))))

walls = set(walls[:1024])
queue = deque([(0, 0, 0)])
visited = set()

while queue:
    x, y, cost = queue.popleft()

    if x == n-1 and y == n-1:
        print(cost)
        break

    if (x, y) in visited:
        continue
    visited.add((x, y))

    for dx, dy in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
        if not (0 <= dx < n and 0 <= dy < n) or (dx, dy) in walls:
            continue

        queue.append((dx, dy, cost+1))