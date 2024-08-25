import re
from z3 import *

class Drone:
    def __init__(self, x, y, z, r) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.rad  = r

    def __repr__(self):
        return f"Drone at ({self.x}, {self.y}, {self.z}) with a radius of {self.rad}"
    
    def inRangeOf(self, other):
        dist = abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)
        return dist <= other.rad

with open("data.txt") as f:
    data = f.read().splitlines()

drones = []
for line in data:
    drones.append(Drone(*[int(x) for x in re.split(r",|>, r=", line.strip("pos=<"))]))

def z3Abs(a):
    return If(a >= 0,a,-a)

o = Optimize()
x, y, z = Ints("x y z")

s = 0
for i, drone in enumerate(drones):
    tracker = Bool(f"t{i}")
    constraint = Implies(tracker, If(x > drone.x, x-drone.x, drone.x-x) + If(y > drone.y, y-drone.y, drone.y-y) + If(z > drone.z, z-drone.z, drone.z-z) <= drone.rad)
    o.add(constraint)
    s = s + If(tracker, 1, 0)

o.maximize(s)
o.minimize(If(x > 0, x, -x) + If(y > 0, y, -y) + If(z > 0, z, -z))

print(o.check())
m = o.model()
print(sum(m[x], m[y], m[z]))
