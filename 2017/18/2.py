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
    def __init__(self, id):
        self.registers = defaultdict(int)
        self.registers["p"] = id
        self.i = 0

    def readValue(self, x):
        if x.strip("-").isdigit():
            return int(x)
        return self.registers[x]
    
    def runProgram(self, inputVals):
        outputVals = []
        while self.i < len(instructions):
            operation, args = instructions[self.i]

            if operation == "snd":
                outputVals.append(self.readValue(args[0]))
            elif operation == "set":
                self.registers[args[0]] = self.readValue(args[1])
            elif operation == "add":
                self.registers[args[0]] += self.readValue(args[1])
            elif operation == "mul":
                self.registers[args[0]] *= self.readValue(args[1])
            elif operation == "mod":
                self.registers[args[0]] %= self.readValue(args[1])
            elif operation == "rcv":
                if inputVals:
                    self.registers[args[0]] = inputVals.pop(0)
                else:
                    return outputVals
            elif operation == "jgz":
                if self.readValue(args[0]) > 0:
                    self.i += self.readValue(args[1])
                    continue

            self.i += 1

        return outputVals
    
comp0 = Computer(0)
comp1 = Computer(1)
res = 0
output0 = comp0.runProgram([])
output1 = comp1.runProgram([])
while output0 or output1:
    res += len(output1)
    output0, output1 = comp0.runProgram(output1), comp1.runProgram(output0)
print(res)

