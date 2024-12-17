from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

def combo(operand):
    if operand < 4:
        return operand
    return regs[operand-4]

def adv(operand):
    regs[0] //= 2**combo(operand)

def bdv(operand):
    regs[1] = regs[0] // 2**combo(operand)

def cdv(operand):
    regs[2] = regs[0] // 2**combo(operand)

def bxl(operand):
    regs[1] ^= operand

def bst(operand):
    regs[1] = combo(operand)%8

def jnz(operand, pnt):
    if regs[0] == 0:
        return pnt
    return operand - 2

def bxc(operand):
    regs[1] ^= regs[2]

def out(operand):
    print(combo(operand)%8, end=",")


with open("data.txt") as f:
    data = f.read().splitlines()

regs = []
for i in range(3):
    _, reg = data[i].split(": ")
    regs.append(int(reg))

OPCODES = [
    adv,
    bxl,
    bst,
    jnz,
    bxc,
    out,
    bdv,
    cdv
]

i = 0
program = [int(x) for x in data[4].strip("Program: ").split(",")]
while i < len(program):
    opcode, operand = program[i], program[i+1]

    if opcode == 3:
        i = OPCODES[opcode](operand, i)
    else:
        OPCODES[opcode](operand)

    i += 2
