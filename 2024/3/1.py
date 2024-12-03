from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read()

def mul(a, b):
    return a*b

res = 0
for match in re.findall(r"mul\([0-9]+,[0-9]+\)", data):
    res += eval(match)

print(res)