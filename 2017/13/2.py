from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

delay = 1
while True:
    found = True
    for row in data:
        time, length = [int(x) for x in row.split(": ")]

        if (time+delay) % ((length-2) * 2 + 2) == 0:
            found = False
            break

    if found:
        print(delay)
        break
    delay += 1