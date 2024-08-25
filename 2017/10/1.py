from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = [int(x) for x in f.read().strip().split(",")]

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

    def getResult(self):
        for _ in range(self.n - (self.rootIndex % self.n)):
            self.prev = self.root
            self.root = self.root.next

        return self.root.val * self.root.next.val
    
    def print(self):
        cur = self.root.next
        res = [self.root.val]

        while cur != self.root:
            res.append(cur.val)
            cur = cur.next

        print(res, self.rootIndex % self.n)

    
ll = LinkedList()
for length in data:
    ll.hash(length)
print(ll.getResult())

             


