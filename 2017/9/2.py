from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().strip("\n")

i = 0
res = 0
isGarbage = False
while i < len(data):
    char = data[i]

    if isGarbage:
        if char == "!":
            i += 1
        elif char == ">":
            isGarbage = False
        else:
            res += 1
    else:
        if char == "<":
            isGarbage = True

    i += 1

print(res)