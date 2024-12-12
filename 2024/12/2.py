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
    peri = set()
    sides = 0

    while stack:
        x, y = stack.popleft()

        if (x, y) in visited:
            continue

        area += 1
        visited.add((x, y))

        for i, (x1, y1) in enumerate([(x+1, y), (x-1, y), (x, y-1), (x, y+1)]):
            if not (0 <= x1 < len(data[0]) and 0 <= y1 < len(data)) or data[y1][x1] != data[y][x]:
                peri.add((x1, y1, i))
                continue

            stack.append((x1, y1))

    for x, y, i in peri:
        if i <= 1 and (x, y+1, i) not in peri:
            sides += 1

        elif i > 1 and (x+1, y, i) not in peri:
            sides += 1
        
    return area * sides

res = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        if (x, y) not in visited:
            res += bfs(x,y) 

print(res)
