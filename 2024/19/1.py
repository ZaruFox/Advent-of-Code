from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    towels, cases = f.read().split("\n\n")
    cases = cases.splitlines()
    towels = towels.split(", ")

@cache
def solve(case, i):
    if i == len(case):
        return True
    
    res = False
    for towel in towels:
        if towel == case[i:len(towel)+i]:
            res |= solve(case, i + len(towel))

    return res

print(sum(solve(case, 0) for case in cases))