from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

DIRECTIONS = {"n": -2j, "s": 2j, "ne": 1-1j, "se": 1+1j, "nw": -1-1j, "sw": -1+1j}

with open("data.txt") as f:
    data = f.read().strip().split(",")

pos = 0 + 0j
res = 0

for direction in data:
    pos += DIRECTIONS[direction]

    x = abs(int(pos.real))
    y = abs(int(pos.imag))
    res = max(res, x + max(0, (y-x) // 2))
print(res)