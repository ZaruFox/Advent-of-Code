from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

adjDict = defaultdict(list)
for row in data:
    v1, v2, dist = re.split(r" = | to ", row)

    adjDict[v1].append((v2, int(dist)))
    adjDict[v2].append((v1, int(dist)))

def dfs(cur, visited):
    if len(visited) == len(adjDict):
        return 0
    
    res = 0
    for v, dist in adjDict[cur]:
        if v in visited:
            continue
        res = max(res, dfs(v, visited | {v})+dist)

    return res

print(max([dfs(v, {v}) for v in adjDict.keys()]))