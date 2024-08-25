from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

password = list("fbgdceah")
#password = list("abcde")

for instruction in data[::-1]:
    splitData = instruction.split()
    if instruction.startswith("rotate right"):
        password = list(numpy.roll(password, -int(splitData[2])))

    elif instruction.startswith("rotate left"):
        password = list(numpy.roll(password, int(splitData[2])))

    elif instruction.startswith("swap position "):
        password[int(splitData[2])], password[int(splitData[5])] = password[int(splitData[5])], password[int(splitData[2])]

    elif instruction.startswith("swap letter"):
        i1 = password.index(splitData[2])
        i2 = password.index(splitData[5])
        password[i1], password[i2] = password[i2], password[i1]

    elif instruction.startswith("rotate based on position of letter "):
        for i in range(len(password)):
            testPass = list(numpy.roll(password, -i))
            rotations = testPass.index(splitData[6]) + (2 if testPass.index(splitData[6]) >= 4 else 1)
            if list(numpy.roll(testPass, rotations)) == password:
                password = testPass
                break

    elif instruction.startswith("move position "):
        password.insert(int(splitData[2]), password.pop(int(splitData[5])))

    elif instruction.startswith("reverse positions "):
        if int(splitData[2]) == 0:
            password = password[int(splitData[4])::-1] + password[int(splitData[4])+1:]
        else:
            password = password[:int(splitData[2])] + password[int(splitData[4]): int(splitData[2])-1:-1] + password[int(splitData[4])+1:]
print("".join(password))