from collections import defaultdict

orbits = defaultdict(list)
with open("data.txt") as f:
    for line in f:
        anchor, orbiting = line.strip().split(")")
        orbits[anchor].append(orbiting)

def dfs(cur, orbitCount=0):
    return orbitCount + sum([dfs(nextPlanet, orbitCount+1) for nextPlanet in orbits[cur]])

print(dfs("COM"))