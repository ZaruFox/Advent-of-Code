from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

steps = 359
res = -1
curPos = 0

for i in range(1, 50000000):
    curPos = ((curPos + steps) % i) + 1
    if curPos == 1:
        res = i
    
print(res)