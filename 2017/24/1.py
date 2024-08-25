from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

connectors = []
adjDict = defaultdict(list)

for i, connector in enumerate(data):
    port1, port2 = [int(x) for x in connector.split("/")]
    adjDict[port1].append((i, port2))
    adjDict[port2].append((i, port1))
    connectors.append((port1, port2))

def dfs(cur, used):
    res = 0
    for i, nextCur in adjDict[cur]:
        if i in used:
            continue
        res = max(nextCur + cur + dfs(nextCur, used | {i}), res)

    return res

print(dfs(0, set()))