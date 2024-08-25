from collections import deque, defaultdict, Counter
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = int(f.readline().strip())

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, size):
        self.root = Node(1, None)
        self.size = size

        cur = self.root
        i = 2
        while True:
            if i == size:
                cur.next = Node(i, self.root)
                break

            cur.next = Node(i, None)
            cur = cur.next
            i += 1

        self.midPrev = self.root
        self.mid = self.root.next
        for _ in range(self.size//2-1):
            self.midPrev = self.mid
            self.mid = self.mid.next

    def playGame(self):
        while self.size != 1:
            self.midPrev.next = self.mid.next
            self.mid = self.mid.next
            
            self.size -= 1

            if self.size % 2 == 0:
                self.midPrev = self.mid
                self.mid = self.mid.next

        return self.root.val
    
print(LinkedList(data).playGame())
    