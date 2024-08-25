from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

res = 0
for row in data:
    time, length = [int(x) for x in row.split(": ")]

    if time % ((length-2) * 2 + 2) == 0:
        res += time * length

print(res)