from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = [int(x) for x in f.read().strip().split()]

@cache
def dp(num, count):
    if count == 0:
        return 1

    if num == 0:
        return dp(1, count-1)

    if len(str(num)) % 2 == 0:
        strLen = len(str(num))
        oriStr = str(num)

        return dp(int(oriStr[strLen//2:]), count-1) + dp(int(oriStr[:strLen//2]), count-1)
    
    return dp(num * 2024, count - 1)

print(sum(dp(x, 75) for x in data))