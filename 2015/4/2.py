from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy
from hashlib import md5

with open("data.txt") as f:
    data = f.read().strip()


i = 1
while True:
    if md5(f"{data}{i}".encode()).hexdigest().startswith("000000"):
        print(i)
        break

    i += 1