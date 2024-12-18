from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    equations, formula = f.read().split("\n\n")

formula = re.findall(r"[A-Z][a-z]?", formula)

print(len(formula) - formula.count("Ar") - formula.count("Rn") - formula.count("Y") * 2 - 1)
            
