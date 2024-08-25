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
res = [None] * 8
while None in res:
    hashVal = hashlib.md5((data+str(i)).encode()).hexdigest()

    if hashVal[:5] == "00000" and hashVal[5].isdigit() and int(hashVal[5]) < 8 and res[int(hashVal[5])] is None:
        res[int(hashVal[5])] = hashVal[6]

        print(res)
    i += 1

print("".join(res))