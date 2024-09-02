from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

totalLength = 0
for present in data:
    dimensions = sorted(map(int, present.split("x")))

    totalLength += 2 * (dimensions[0] + dimensions[1]) + math.prod(dimensions)

print(totalLength)