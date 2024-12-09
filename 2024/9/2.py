from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read()

files = []
heaps = [[] for _ in range(10)]

j = 0
for i, size in enumerate(data):
    size = int(size)

    if i % 2 == 0:
        files.append((i//2, j, size))
    else:
        heappush(heaps[size], j)

    j += size

res = 0
for id, i, size in files[::-1]:
    
    heapSize = None 
    k = math.inf
    for emptySize in range(size, 10):
        if (not heaps[emptySize]) or heaps[emptySize][0] >= i:
            continue

        if heaps[emptySize][0] < k:
            heapSize = emptySize
            k = heaps[emptySize][0]

    if heapSize is None:
        res += sum(range(i, i + size)) * id
    else:      
        j = heappop(heaps[heapSize])
        res += sum(range(j, j + size)) * id
        heappush(heaps[heapSize-size], j+size)

print(res)