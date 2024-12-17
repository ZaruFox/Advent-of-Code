from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read()

res = 0
for match in re.findall(r"-?\d+", data):
    res += int(match)
print(res)