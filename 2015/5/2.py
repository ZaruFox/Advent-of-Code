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
    if re.search(r"([a-z][a-z]).*\1", string) and re.search(r"(.).\1", string):
        res += 1

print(res)