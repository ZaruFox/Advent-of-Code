from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

INVALID = ("ab", "cd", "pq", "xy")
VOWELS = ("a", "e", "i", "o", "u")

res = 0

for string in data:
    if any(x in string for x in INVALID):
        continue

    if sum(string.count(x) for x in VOWELS) < 3:
        continue

    if not re.search(r"([a-z])\1+", string):
        continue

    res += 1

print(res)