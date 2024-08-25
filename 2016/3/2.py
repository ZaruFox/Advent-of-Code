from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = [[int(x) for x in line.split()] for line in f.read().splitlines()]

triangles = []
for i in range(0, len(data), 3):
    for j in range(3):
        triangles.append(sorted((data[i][j], data[i+1][j], data[i+2][j])))

res = 0

for lengths in triangles:
    if lengths[0] + lengths[1] > lengths[2]:
        res += 1
    
print(res)

    