from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.readline().strip()

def findLength(i, maxI):
    currentLen = 0

    while i <= maxI:
        if data[i] == "(":
            i += 1
            marker = ""

            while data[i] != ")":
                marker += data[i]
                i += 1

            length, times = [int(x) for x in marker.split("x")]
            currentLen += times * findLength(i+1, i + length)
            i += length + 1

        else:
            currentLen += 1
            i += 1

    return currentLen

print(findLength(0, len(data)-1))
            

