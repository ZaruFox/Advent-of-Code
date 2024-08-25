from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = int(f.read().strip())

length = 1
while True:
    if length == 1:
        perimeter = 1
    else:
        perimeter = (length-1) * 4

    if data <= perimeter:
        data -= 1
        data %= length-1
        mid = length // 2 - 1
        print((length // 2) + abs(mid - data))
        break
    else:
        data -= perimeter
        length += 2

    
