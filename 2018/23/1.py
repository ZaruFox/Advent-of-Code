import re

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

targetDrone = max(drones, key = lambda x: x.rad)

print(sum([drone.inRangeOf(targetDrone) for drone in drones]))