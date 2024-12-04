from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

letters = ["X", "M", "A", "S"]
res = 0
# i hate this
for y in range(len(data)):
    for x in range(len(data[0])):
        for direction in ((-1, -1), (1, -1), (-1, 1), (1, 1), (0, 1), (0, -1), (1, 0), (-1, 0)):
            x1, y1 = x, y
            matched = True
            for letter in letters:
                if not (0 <= x1 < len(data[0]) and 0 <= y1 < len(data)) or data[y1][x1] != letter:
                    matched = False
                    break

                x1 += direction[0]
                y1 += direction[1]

            if matched:
                res += 1


print(res)