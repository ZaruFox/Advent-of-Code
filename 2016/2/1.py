from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

DIRECTIONS = {"U":-1j, "D":1j, "L":-1, "R":1}
curPos = 1 + 1j

code = ""
for instructions in data:
    for direction in instructions:
        newPos = curPos + DIRECTIONS[direction]

        if 0 <= int(newPos.imag) <= 2 and 0 <= int(newPos.real) <= 2:
            curPos = newPos

    code += str(int(curPos.imag) * 3 + int(curPos.real) + 1)

print(code)