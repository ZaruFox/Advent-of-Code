from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().strip()

class Node:
    def __init__(self, val, next = None) -> None:
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, n=256):
        self.root = Node(0)
        self.n = n

        cur = self.root
        for i in range(1, n):
            cur.next = Node(i)
            cur = cur.next
        cur.next = self.root

        self.prev = cur
        self.rootIndex = 0
        self.skipSize = 0

    def hash(self, length):
        
        self.rootIndex += length + self.skipSize
        
        if length != 0:
            oriPrev = self.prev
            oriRoot = self.root

            self.prev = self.root
            self.root = self.root.next
            for _ in range(length-1):
                tmp = self.root.next
                self.root.next, self.root, self.prev = self.prev, tmp, self.root

            if length != self.n:
                oriPrev.next, self.prev = self.prev, oriRoot
                oriRoot.next = self.root
            else:
                oriRoot.next = self.prev
                self.prev, self.root = self.root, self.prev 

        for _ in range(self.skipSize):
            self.prev = self.root
            self.root = self.root.next
        self.skipSize += 1
        
        assert self.prev.next == self.root

    def getList(self):
        for _ in range(self.n - (self.rootIndex % self.n)):
            self.prev = self.root
            self.root = self.root.next

        res = []
        for _ in range(self.n):
            res.append(self.root.val)
            self.root = self.root.next

        return res
    
def knotHash(str):
    lengths = [ord(x) for x in str] + [17, 31, 73, 47, 23]
    ll = LinkedList()
    for _ in range(64):
        for length in lengths:
            ll.hash(length)

    sparseHash = ll.getList()
    denseHash = ""
    for i in range(0, len(sparseHash), 16):
        tmp = sparseHash[i]
        for j in range(i+1, i+16):
            tmp ^= sparseHash[j]
        denseHash += f"{tmp:02x}"
    
    return denseHash

res = 0
for row in range(128):
    hashed = knotHash(f"{data}-{row}")
    for hexValue in hashed:
        res += f"{int(hexValue, base=16):04b}".count("1")

print(res)