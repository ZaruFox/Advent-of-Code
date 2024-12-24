from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

a = 0
b = 0
i = 0

while i < len(data):
    opcode, operand = data[i][:3], data[i][4:]

    if opcode == "hlf":
        exec(f"{operand} //= 2")
        i += 1

    elif opcode == "tpl":
        exec(f"{operand} *= 3")
        i += 1

    elif opcode == "tpl":
        exec(f"{operand} *= 3")
        i += 1

    elif opcode == "inc":
        exec(f"{operand} += 1")
        i += 1

    elif opcode == "tpl":
        exec(f"{operand} *= 3")
        i += 1

    elif opcode == "jmp":
        exec(f"i += {operand}")

    elif opcode == "jie":
        register, offset = operand.split(", ")

        if eval(register) % 2 == 0:
            exec(f"i += {offset}")
        else:
            i += 1

    elif opcode == "jio":
        register, offset = operand.split(", ")

        if eval(register) == 1:
            exec(f"i += {offset}")
        else:
            i += 1

print(b)