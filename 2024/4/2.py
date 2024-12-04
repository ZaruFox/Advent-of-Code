from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

res = 0

for y in range(1, len(data)-1):
    for x in range(1, len(data[0])-1):
        if data[y][x] == "A":
            corners = data[y-1][x-1] + data[y-1][x+1] + data[y+1][x+1] + data[y+1][x-1]

            if corners in ("MMSS", "SMMS", "SSMM", "MSSM"):
                res += 1


print(res)