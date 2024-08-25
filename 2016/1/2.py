from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().strip().split(", ")

DIRECTIONS = [-1j, 1, 1j, -1]
curDirection = 0
curPos = 0 + 0j
visited = set()

for move in itertools.cycle(data):
    if move.startswith("L"):
        curDirection -= 1
    else:
        curDirection += 1

    curDirection %= 4

    for _ in range(int(move.strip("LR"))):
        if curPos in visited:
            print(int(abs(curPos.real) + abs(curPos.imag)))
            exit()
        visited.add(curPos)
        curPos += DIRECTIONS[curDirection]