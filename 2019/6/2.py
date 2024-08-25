from collections import defaultdict, deque
import sys

orbits = defaultdict(list)
with open("data.txt") as f:
    for line in f:
        anchor, orbiting = line.strip().split(")")
        orbits[anchor].append(orbiting)
        orbits[orbiting].append(anchor)

queue = deque([("YOU", 0)])
visited = {"YOU"}

while queue:
    cur, pathCost = queue.popleft()

    for nextPlanet in orbits[cur]:
        if nextPlanet == "SAN":
            print(pathCost-1)
            sys.exit()
            
        if nextPlanet in visited:
            continue
        visited.add(nextPlanet)

        queue.append((nextPlanet, pathCost+1))