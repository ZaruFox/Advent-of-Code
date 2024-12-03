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
enabled = True
for match in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data):
    if match == "do()":
        enabled = True
    elif match == "don't()":
        enabled = False
    elif enabled:
        res += eval(match)

print(res)