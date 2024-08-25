from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().strip().split(",")

dancers = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
for instruction in data:
    if instruction[0].startswith("s"):
        x = int(instruction[1:])
        dancers = dancers[-x:] + dancers[:-x]

    elif instruction[0].startswith("x"):
        i1, i2 = [int(x) for x in instruction[1:].split("/")]
        dancers[i1], dancers[i2] = dancers[i2], dancers[i1]

    else:
        i1, i2 = [dancers.index(x) for x in instruction[1:].split("/")]
        dancers[i1], dancers[i2] = dancers[i2], dancers[i1]

print("".join(dancers))


