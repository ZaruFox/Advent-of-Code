from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

target = (2947, 3029)


nth = 1 + sum(range(2, target[1]+1)) + sum(range(target[1], target[0]+target[1]-1))

i = 20151125
for _ in range(1, nth):
    i *= 252533
    i %= 33554393
print(i)