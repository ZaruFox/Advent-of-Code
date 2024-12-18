from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy
from sympy import divisors

with open("data.txt") as f:
    target = int(f.read())

i = 0
while True:
    total = 0
    for num in divisors(i):
        if i // num > 50:
            continue

        total += num * 11

    if total >= target:
        print(i)
        break

    i += 1