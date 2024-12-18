from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    equations, formula = f.read().split("\n\n")

equationsMap = defaultdict(list)
for equation in equations.splitlines():
    e1, e2 = equation.split(" => ")
    equationsMap[e1].append(e2)

formula = re.findall(r"[A-Z][a-z]?", formula)
seen = set()

for i, original in enumerate(formula):
    for new in equationsMap[original]:
        formula[i] = new
        if "".join(formula) not in seen:
            seen.add("".join(formula))
        
    formula[i] = original

print(len(seen))