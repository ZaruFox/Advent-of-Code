from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

def cpy(registers, x, y):
    registers[y] = registers[x] if x.isalpha() else int(x)

def inc(registers, x):
    registers[x] += 1

def dec(registers, x):
    registers[x] -= 1

FUNCTIONS = {"cpy": cpy, "inc": inc, "dec": dec}

i = 0
registers = {"a": 0, "b": 0, "c": 1, "d": 0}
while i < len(data):
    if i == 12:
        registers["a"] += registers["b"]
        registers["b"] = 0

    instruction = data[i].split()
    if instruction[0] == "jnz":
        if (registers[instruction[1]] if instruction[1].isalpha() else int(instruction[1])) != 0:
            i += int(instruction[2])
        else:
            i += 1
    else:
        FUNCTIONS[instruction[0]](registers, *instruction[1:])
        i += 1

print(registers["a"])
