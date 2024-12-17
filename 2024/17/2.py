from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

program = [int(x) for x in data[4].strip("Program: ").split(",")]

def dfs(i, a):
    if i == -1:
        return [a]
    
    a <<= 3
    res = []
    for b in range(8):
        a += b

        temp = b ^ 7
        temp ^= a >> temp
        temp ^= 4

        if temp % 8 == program[i]:
            res += dfs(i-1, a)
        
        a -= b

    return res

print(min(dfs(len(program)-1, 0)))



# 2,4,1,7,7,5,4,1,1,4,5,5,0,3,3,0
"""
while A != 0:

    B = A % 8   # get last 3 bits of A
    B ^= 7      # flip all bits

    B ^= A // (2**B)  # flip B according to truncated A
    B ^= 4  # flip 2nd bit
    print(B % 8) # print last 3 bits of B

    A //= 2**3  # truncate last 3 bits of A
"""
