from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

robots = []

n = 103
m = 101

for line in data:
    robots.append([int(x) for x in re.split(r",| v=", line.strip("p="))])

quadrants = [0, 0, 0, 0]
for x, y, dx, dy in robots:
    newX = (x + dx*100) % m
    newY = (y + dy*100) % n

    if newX <= 49 and newY <= 50:
        quadrants[0] += 1
    elif newX > 50 and newY <= 50:
        quadrants[1] += 1
    elif newX <= 49 and newY > 51:
        quadrants[2] += 1
    elif newX > 50 and newY > 51:
        quadrants[3] += 1

print(math.prod(quadrants))
    
