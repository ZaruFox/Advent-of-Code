from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

def validate(ip):
    hypernet = False
    aba = []
    bab = []

    for i in range(len(ip)-2):
        if ip[i] == "[":
            hypernet = True

        elif ip[i] == "]":
            hypernet = False

        elif ip[i] == ip[i+2] and ip[i] != ip[i+1]:
            if hypernet:
                if (ip[i+1], ip[i]) in aba:
                    return True
                
                bab.append((ip[i], ip[i+1]))

            else:
                if (ip[i+1], ip[i]) in bab:
                    return True
                
                aba.append((ip[i], ip[i+1]))


    return False
            

with open("data.txt") as f:
    data = f.read().splitlines()

print(sum([1 for ip in data if validate(ip)]))
