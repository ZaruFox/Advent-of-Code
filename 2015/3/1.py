from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().strip()


DIRECTIONS = {">": (1, 0), "<": (-1, 0), "v": (0, 1), "^": (0, -1)}

visited = {(0, 0)}
cur = [0, 0]

for direction in data:
    dX, dY = DIRECTIONS[direction]

    cur[0] += dX
    cur[1] += dY

    if tuple(cur) not in visited:
        visited.add(tuple(cur))

print(len(visited))