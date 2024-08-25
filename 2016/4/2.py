from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

for row in data:
    row, checksum = row.strip("]").split("[")
    row = row.split("-")
    _hash, _id = list("".join(row[:-1])), int(row[-1])

    count = Counter(_hash)
    sortedHash = sorted(count.keys(), key=lambda x: (-count[x], x))

    if list(checksum) == sortedHash[:5]:
        _hash = list(" ".join(row[:-1]))
        for i in range(len(_hash)):
           if _hash[i] == " ":
               continue
           _hash[i] = chr(((ord(_hash[i]) - 97 + _id) % 26) + 97)

        if "northpole" in "".join(_hash):
            print(_id)
            break
