from collections import deque, defaultdict, Counter
import re
from functools import cache, reduce
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("test.txt") as f:
    data = f.read().splitlines()

adjDict = defaultdict(set)
for row in data:
    a, b = row.split("-")
    
    adjDict[a].add(b)
    adjDict[b].add(a)

groups = []

for node in adjDict:
    for group in groups:
        if group.issubset(adjDict[node]):
            groups.append(group | {node})
    
    groups.append({node})

print(",".join(sorted(max(groups, key=len))))