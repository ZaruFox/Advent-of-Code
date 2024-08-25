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
for row in data:
    row, checksum = row.strip("]").split("[")
    row = row.split("-")
    _hash, _id = "".join(row[:-1]), int(row[-1])

    count = Counter(_hash)
    sortedHash = sorted(count.keys(), key=lambda x: (-count[x], x))

    if list(checksum) == sortedHash[:5]:
        res += _id

print(res)
    