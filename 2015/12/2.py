from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy
import json

with open("data.txt") as f:
    data = json.load(f)

def getSum(iter):
    if type(iter) == dict:
        iter = iter.values()
        if "red" in iter:
            return 0

    res = 0
    for item in iter:
        try:
            res += int(item)
        except:
            if type(item) != str:
                res += getSum(item)

    return res

print(getSum(data))