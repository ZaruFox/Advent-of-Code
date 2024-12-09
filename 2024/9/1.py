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
for i, size in enumerate(data):
    files.append([i//2 if i % 2 == 0 else -1, int(size)])

l, r = 0, len(files) - 1
i = 0
res = 0

while l < r:
    id, size = files[l]
    l += 1
    
    if id != -1:
        res += sum(range(i, i+size)) * id
        i += size
        continue

    for _ in range(size):
        res += i * files[r][0]
        i += 1
        files[r][1] -= 1

        if files[r][1] == 0:
            r -= 2

            if r < l:
                break

            
    

print(res)