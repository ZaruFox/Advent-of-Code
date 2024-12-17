from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    cups = [int(x) for x in f.read().splitlines()]

@cache
def dp(remaining, i):
    if remaining == 0:
        return 1
    
    if i == len(cups):
        return 0
    
    res = 0
    for j in range(i+1, len(cups)):
        res += dp(remaining-cups[j], j)

    return res

print(sum(dp(150-cups[i], i) for i in range(len(cups))))