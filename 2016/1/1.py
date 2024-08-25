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

for move in data:
    if move.startswith("L"):
        curDirection -= 1
    else:
        curDirection += 1

    curDirection %= 4

    curPos += DIRECTIONS[curDirection] * int(move.strip("LR"))

print(int(abs(curPos.real) + abs(curPos.imag)))