from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy
from sympy import divisors

with open("data.txt") as f:
    target = int(f.read()) // 10

i = 0
while True:
    if sum(divisors(i)) >= target:
        print(i)
        break

    i += 1