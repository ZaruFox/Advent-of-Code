from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

instructions = []

for instruction in data:
    operation, *args = instruction.split(" ")
    instructions.append((operation, args))

class Computer:
    def __init__(self):
        self.registers = defaultdict(int)
        self.i = 0

    def readValue(self, x):
        if x.strip("-").isdigit():
            return int(x)
        return self.registers[x]
    
    def runProgram(self):
        res = 0
        while self.i < len(instructions):
            operation, args = instructions[self.i]

            if operation == "set":
                self.registers[args[0]] = self.readValue(args[1])
            elif operation == "sub":
                self.registers[args[0]] -= self.readValue(args[1])
            elif operation == "mul":
                res += 1
                self.registers[args[0]] *= self.readValue(args[1])
            elif operation == "jnz":
                if self.readValue(args[0]) != 0:
                    self.i += self.readValue(args[1])
                    continue

            self.i += 1

        return res
    
print(Computer().runProgram())


