from bisect import bisect_left
from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

walls = []
for line in data:
    walls.append(tuple(map(int, line.split(","))))

def bfs(walls):
    n = 71
    queue = deque([(0, 0, 0)])
    visited = set()

    while queue:
        x, y, cost = queue.popleft()

        if x == n-1 and y == n-1:
            return False

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
            if not (0 <= dx < n and 0 <= dy < n) or (dx, dy) in walls:
                continue

            queue.append((dx, dy, cost+1))

    return True

pos = bisect_left(range(len(walls)), 1, key=lambda i: bfs(walls[:i+1]))
print(",".join(str(x) for x in walls[pos]))