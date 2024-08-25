from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

class Bot:
    bots = {}
    output = [0] * 21

    def __init__(self, _id, minI, minOutput, maxI, maxOutput):
        self.values = []
        self._id = _id
        self.min = minI
        self.minOutput = minOutput
        self.max = maxI
        self.maxOutput = maxOutput

    def add(self, val):
        self.values.append(val)

        if len(self.values) == 2:
            if 61 in self.values and 17 in self.values:
                print(self._id)

            if self.minOutput:
                Bot.output[self.min] = min(self.values)
            else:
                Bot.bots[self.min].add(min(self.values))

            if self.maxOutput:
                Bot.output[self.max] = max(self.values)
            else:
                Bot.bots[self.max].add(max(self.values))


with open("data.txt") as f:
    data = f.read().splitlines()

for row in data:
    row = row.split()

    if row[0] == "bot":
        Bot.bots[int(row[1])] = Bot(int(row[1]), int(row[6]), row[5] == "output", int(row[11]), row[10] == "output")

for row in data:
    row = row.split()

    if row[0] == "value":
        Bot.bots[int(row[-1])].add(int(row[1]))

