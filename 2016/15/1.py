from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

class Disc:
    def __init__(self, _id, positionCount, starting) -> None:
        self.starting = starting
        self.positionCount = positionCount
        self._id = _id

    def getPosition(self, startTime):
        return (startTime + self.starting + self._id) % self.positionCount

with open("data.txt") as f:
    data = f.read().splitlines()    

discs = []
for i in range(len(data)):
    discs.append(Disc(*[int(x) for x in re.split(r"Disc #| has | positions; at time=0, it is at position |\.", data[i])[1:-1]]))

time = 0
while True:
    if all(disc.getPosition(time) == 0 for disc in discs):
        print(time)
        break
    time += 1