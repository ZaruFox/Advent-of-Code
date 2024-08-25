from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

res = 0

for lengths in data:
    lengths = sorted([int(x) for x in lengths.split()])

    if lengths[0] + lengths[1] > lengths[2]:
        res += 1
    
print(res)

    