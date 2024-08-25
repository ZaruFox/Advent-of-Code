from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

steps = 359
buffer = [0]
curPos = 0

for i in range(1, 2018):
    curPos = ((curPos + steps) % i) + 1
    buffer.insert(curPos, i)

print(buffer[buffer.index(2017) + 1])