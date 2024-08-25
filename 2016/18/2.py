from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = list("." + f.readline().strip() + ".")

grid = [data]
visited = {}
for _ in range(400000-1):
    newRow = ["."]
    for i in range(1, len(grid[-1])-1):
        if grid[-1][i-1:i+2] in (["^", "^", "."], [".", "^", "^"], ["^", ".", "."], [".", ".", "^"]):
            newRow.append("^")
        else:
            newRow.append(".")
    newRow += ["."]

    grid.append(newRow)

print(sum([x[1:-1].count(".") for x in grid]))
