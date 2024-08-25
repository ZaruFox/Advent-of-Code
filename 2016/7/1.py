from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

def validate(ip):
    found = False
    hypernet = False

    for i in range(len(ip)-3):
        if ip[i] == "[":
            hypernet = True

        elif ip[i] == "]":
            hypernet = False

        elif ip[i] == ip[i+3] and ip[i+1] == ip[i+2] and ip[i] != ip[i+1]:
            if hypernet:
                return False
            else:
                found = True

    return found
            

with open("data.txt") as f:
    data = f.read().splitlines()

print(sum([1 for ip in data if validate(ip)]))
