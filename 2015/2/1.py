from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

totalArea = 0
for present in data:
    l, w, h = map(int, present.split("x"))
    sides = (l*w, w*h, l*h)

    totalArea += 2 * sum(sides) + min(sides)

print(totalArea)