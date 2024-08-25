from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

adjDict = defaultdict(lambda: [-1, []])

for row in data:
    row = row.split(" -> ")
    name, weight = row[0].strip(")").split(" (")
    adjDict[name][0] = int(weight)

    if len(row) == 2:
        adjDict[name][1] = row[1].split(", ")

childrenSet = set()
for _, children in adjDict.values():
    childrenSet.update(set(children))

print((adjDict.keys() ^ childrenSet).pop())