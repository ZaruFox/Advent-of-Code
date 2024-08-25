from collections import deque, defaultdict
import re
from functools import cache
import itertools
from heapq import heappop, heappush
import math
import numpy

with open("data.txt") as f:
    data = f.read().splitlines()

class Particle:
    def __init__(self, x, y, z, dx, dy, dz, d2x, d2y, d2z):
        self.pos = [x, y, z]
        self.vel = [dx, dy, dz]
        self.acc = (d2x, d2y, d2z)

    def move(self): 
        for i in range(3):
            self.vel[i] += self.acc[i]
            self.pos[i] += self.vel[i]

    def distanceFromOrigin(self):
        return sum([abs(x) for x in self.pos])

particles = []
for row in data:
    particles.append(Particle(*[int(x) for x in re.split(r",|>, [av]=<", row.strip("p=<>"))]))

for i in range(500):
    for particle in particles:
        particle.move()

print(min(range(len(particles)), key = lambda i: particles[i].distanceFromOrigin() ))