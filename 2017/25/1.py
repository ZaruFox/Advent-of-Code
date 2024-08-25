from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

curState = "A"
vals = defaultdict(int)
i = 0

for _ in range(12261543):
    if curState == "A":
        if vals[i] == 0:
            vals[i] = 1
            i += 1
            curState = "B"

        else:
            vals[i] = 0
            i -= 1
            curState = "C"

    elif curState == "B":
        if vals[i] == 0:
            vals[i] = 1
            i -= 1
            curState = "A"

        else:
            vals[i] = 1
            i += 1
            curState = "C"

    elif curState == "C":
        if vals[i] == 0:
            vals[i] = 1
            i += 1
            curState = "A"

        else:
            vals[i] = 0
            i -= 1
            curState = "D"

    elif curState == "D":
        if vals[i] == 0:
            vals[i] = 1
            i -= 1
            curState = "E"

        else:
            vals[i] = 1
            i -= 1
            curState = "C"

    elif curState == "E":
        if vals[i] == 0:
            vals[i] = 1
            i += 1
            curState = "F"

        else:
            vals[i] = 1
            i += 1
            curState = "A"

    elif curState == "F":
        if vals[i] == 0:
            vals[i] = 1
            i += 1
            curState = "A"

        else:
            vals[i] = 1
            i += 1
            curState = "E"

print(list(vals.values()).count(1))