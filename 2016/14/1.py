from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy
import hashlib

@cache
def getMD5(string: str):
    return hashlib.md5(string.encode()).hexdigest()

def findRecurringValues(string, recurringTarget):
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
            
            if count == recurringTarget:
                return string[i]
        else:
            count = 1

    return ""
        
with open("data.txt") as f:
    data = f.readline().strip()

i = 0
keyNumber = 0
while True:
    hash1 = getMD5(f"{data}{i}")

    if target := findRecurringValues(hash1, 3):
        target *= 5

        for j in range(i + 1, i + 1001):
            if target in getMD5(f"{data}{j}"):
                keyNumber += 1
                print(f"Key {keyNumber} found!")

                if keyNumber == 64:
                    print(i)
                    exit()

                break

    i += 1
