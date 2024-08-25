from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

adjDict = {}
for relationship in data:
    origin, neighbours = relationship.split(" <-> ")
    adjDict[origin] = neighbours.split(", ")

queue = deque(["0"])
visited =  {"0"}

while queue:
    cur = queue.popleft()

    for adj in adjDict[cur]:
        if adj in visited:
            continue
        visited.add(adj)

        queue.append(adj)

print(len(visited))