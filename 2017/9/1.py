from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("test.txt") as f:
    data = f.read().strip("\n")

score = 1
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
        if char == "{":
            res += score
            score += 1
        elif char == "<":
            isGarbage = True
        elif char == "}":
            score -= 1

    i += 1

print(res)