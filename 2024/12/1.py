from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

visited = set()

def bfs(startX, startY):
    stack = deque([(startX, startY)])

    area = 0
    peri = 0

    while stack:
        x, y = stack.popleft()

        if (x, y) in visited:
            continue
        area += 1
        visited.add((x, y))

        for x1, y1 in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
            if not (0 <= x1 < len(data[0]) and 0 <= y1 < len(data)) or data[y1][x1] != data[y][x]:
                peri += 1
                continue

            stack.append((x1, y1))

    return area * peri

res = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        if (x, y) not in visited:
            res += bfs(x,y) 

print(res)
