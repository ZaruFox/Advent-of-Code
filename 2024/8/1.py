from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

def findAntinodes(x1, y1, x2, y2):
    dx = x2-x1
    dy = y2-y1

    return {(x1-dx, y1-dy), (x2+dx, y2+dy)}

with open("data.txt") as f:
    data = f.read().splitlines()

antennnas = defaultdict(list)
for y, row in enumerate(data):
    for x, char in enumerate(row):
        if char != ".":
            antennnas[char].append((x, y))

antinodes = set()
for locations in antennnas.values():
    for i in range(len(locations)):
        for j in range(i+1, len(locations)):
            antinodes |= findAntinodes(*locations[i], *locations[j])

print(len([(x, y) for x, y in antinodes if 0 <= x < len(data[0]) and 0 <= y < len(data)]))