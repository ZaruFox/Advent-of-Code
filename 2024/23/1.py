from collections import deque, defaultdict, Counter
import re
from functools import cache, reduce
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

adjDict = defaultdict(set)
for row in data:
    a, b = row.split("-")
    
    adjDict[a].add(b)
    adjDict[b].add(a)

def dfs(cur, visited):
    res = set()
    for next in adjDict[cur]:
        if next not in visited and all(x in adjDict[next] for x in visited):
            newVisited = visited | {next}
            if len(newVisited) == 3 and any(x.startswith("t") for x in newVisited):
                res.add(tuple(sorted(newVisited)))

            elif len(newVisited) != 3:
                res |= dfs(next, newVisited)

    return res

print(len(reduce(lambda a, b: a | b, [dfs(x, set([x])) for x in adjDict])))