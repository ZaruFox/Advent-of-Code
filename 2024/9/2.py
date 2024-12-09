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
id = 0
empty = False

for num in data:
    num = int(num)
    if not empty:
        files.append([id, num])
        id += 1
    else:
        files.append([-1, num])

    empty = not empty

j = len(files)-1
while j > 0:
    id, count = files[j]

    if id == -1:
        j -= 1
        continue

    for i, file in enumerate(files[:j]):
        newId, newCount = file
        if newId == -1 and newCount >= count:
            files[j][0] = -1
            if newCount != count:
                if files[i+1][0] == -1:
                    files[i+1][1] += newCount-count
                else:
                    files.insert(i+1, [-1, newCount-count])
                    j += 1
            files[i] = [id, count]
            break

    j -= 1

res = 0
i = 0
for id, count in files:
    if id != -1:
        res += sum(range(i, i+count)) * id
    i += count
    
print(res)