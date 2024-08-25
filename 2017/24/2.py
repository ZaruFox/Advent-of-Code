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

queue = deque([(0, set(), 0)])
maxLength = 0
res = 0

while queue:
    cur, visited, val = queue.popleft()

    if len(visited) > maxLength:
        res = val 
        maxLength = len(visited)

    elif len(visited) == maxLength:
        res = max(res, val)

    for i, next in adjDict[cur]:
        if i in visited:
            continue
        queue.append((next, visited | {i}, val + cur + next))

print(res)