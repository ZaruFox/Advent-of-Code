from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read()

files = deque()
i = 0
empty = False

for num in data:
    num = int(num)
    if not empty:
        files.append([i, num])
        i += 1
    else:
        files.append([-1, num])

    empty = not empty

i = 0
res = 0

while files:
    id, count = files.popleft()
    
    if id != -1:
        res += sum(range(i, i+count)) * id
        i += count
    else:
        while files and count > 0:
            if files[-1][0] == -1:
                files.pop()
                continue
            
            totalRemoved = min(count, files[-1][1])
            res += sum(range(i, i+totalRemoved)) * files[-1][0]
            i += totalRemoved
            files[-1][1] -= totalRemoved
            count -= totalRemoved
            if files[-1][1] == 0:
                files.pop()
            
    

print(res)