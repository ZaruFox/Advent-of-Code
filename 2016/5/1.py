from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy
import hashlib

with open("data.txt") as f:
    data = f.readline().strip()

i = 0
res = ""
while len(res) < 8:
    hashVal = hashlib.md5((data+str(i)).encode())

    if hashVal.hexdigest()[:5] == "00000":
        res += hashVal.hexdigest()[5]
    i += 1

print(res)