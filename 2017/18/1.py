from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

regisiters = defaultdict(int)
lastSound = -1
instructions = []

for instruction in data:
    operation, *args = instruction.split(" ")
    instructions.append((operation, args))

def readValue(x):
    if x.strip("-").isdigit():
        return int(x)
    return regisiters[x]

i = 0
while i < len(instructions):
    operation, args = instructions[i]

    if operation == "snd":
        lastSound = readValue(args[0])
    elif operation == "set":
        regisiters[args[0]] = readValue(args[1])
    elif operation == "add":
        regisiters[args[0]] += readValue(args[1])
    elif operation == "mul":
        regisiters[args[0]] *= readValue(args[1])
    elif operation == "mod":
        regisiters[args[0]] %= readValue(args[1])
    elif operation == "rcv":
        if readValue(args[0]) != 0:
            print(lastSound)
            break
    elif operation == "jgz":
        if readValue(args[0]) > 0:
            i += readValue(args[1])
            continue

    i += 1

