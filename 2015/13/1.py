from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

rels = defaultdict(dict)
for line in data:
    line = line.replace("lose ", "-")
    line = line.replace("gain ", "")
    a, value, b = re.split(" would | happiness units by sitting next to ", line.strip("."))
    
    rels[a][b] = int(value)
    
res = 0
for order in itertools.permutations(rels.keys()):
    currentScore = 0
    for i, name in enumerate(order):
        currentScore += rels[name][order[(i+1)%len(order)]]
        currentScore += rels[name][order[(i-1)%len(order)]]

    res = max(currentScore, res)

print(res)