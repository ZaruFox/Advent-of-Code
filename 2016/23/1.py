from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = [x.split() for x in f.read().splitlines()]

def parse(registers, x):
    return (registers[x] if x.isalpha() else int(x))

def cpy(registers, x, y):
    registers[y] = parse(registers, x)

def inc(registers, x):
    registers[x] += 1

def dec(registers, x):
    registers[x] -= 1

FUNCTIONS = {"cpy": cpy, "inc": inc, "dec": dec}
INVERSE = {"cpy": "jnz", "jnz": "cpy", "inc": "dec", "dec": "inc", "tgl": "inc"}

i = 0
registers = {"a": 7, "b": 0, "c": 0, "d": 0}
while i < len(data):
    cmd, *args = data[i]

    if cmd == "jnz" and parse(registers, args[0]) != 0:
        i += parse(registers, args[1])
        continue

    elif cmd == "tgl":
        target = parse(registers, args[0]) + i
        if target < len(data):
            data[target][0] = INVERSE[data[target][0]]
        
    elif cmd != "jnz":
        FUNCTIONS[cmd](registers, *args)

    i += 1

print(registers["a"])