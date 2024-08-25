from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

ranges = []

for row in data:
    ranges.append([int(x) for x in row.split("-")])

ranges.sort(key = lambda x:x[0])

i = 1
while i < len(ranges):
    if ranges[i][0] <= ranges[i-1][1]+1:
       l, r = ranges.pop(i)
       ranges[i-1][1] = max(r, ranges[i-1][1])
    else:
        i += 1

print(ranges[0][1]+1)
    
