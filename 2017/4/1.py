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
for passphrase in data:
    passphrase = passphrase.split()

    if len(passphrase) == len(set(passphrase)):
        res += 1

print(res)