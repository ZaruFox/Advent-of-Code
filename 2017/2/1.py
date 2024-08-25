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
    numbers = [int(x) for x in row.split()]
    res += max(numbers) - min(numbers)
print(res)
