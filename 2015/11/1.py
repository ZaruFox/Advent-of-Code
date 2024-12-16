from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().strip()

def addOne(password):
    password[-1] += 1
    i = -1

    while password[i] == 26:
        password[i] = 0
        i -= 1
        password[i] += 1

def isValid(password):
    for invalidLetter in ("o", "i", "l"):
        if ord(invalidLetter)-ord("a") in password:
            return False
        
    diff = [str(password[i]-password[i-1]) for i in range(1, len(password))]
    if diff.count("0") < 2:
        return False
    
    diff = ",".join(diff)
    if ",0,0," in diff or diff.endswith(",0,0"):
        return False
    
    if ",1,1," not in diff and not diff.endswith(",1,1"):
        return False
    
    return True
    

password = [ord(char) - ord("a") for char in data]
while True:
    addOne(password)

    if isValid(password):
        print("".join([chr(x+ord("a")) for x in password]))
        break