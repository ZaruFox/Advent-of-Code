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
for match in re.findall(r"mul\(\d+,\d+\)", data):
    res += eval(match)

print(res)