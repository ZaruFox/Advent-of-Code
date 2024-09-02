from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().strip()

floor = 0
for i in range(len(data)):
    if data[i] == "(":
        floor += 1
    else:
        floor -= 1

    if floor == -1:
        print(i+1)
        break
    