from collections import defaultdict

bugs = set()

with open("data.txt") as f:
    grid = [x.strip() for x  in f.readlines()]

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "#":
            bugs.add((x, y))


visited = set()
while True:
    adjBugs = defaultdict(int)

    for bugX, bugY in bugs:
        for adj in ((bugX, bugY+1), (bugX, bugY-1), (bugX+1, bugY), (bugX-1, bugY)):
            if 0 <= adj[0] < len(grid[0]) and 0 <= adj[1] < len(grid):
                adjBugs[adj] += 1

    newBugs = set()
    for location, adjBugsCount in adjBugs.items():
        if location in bugs and adjBugsCount == 1:
            newBugs.add(location)
        elif location not in bugs and 1 <= adjBugsCount <= 2:
            newBugs.add(location)

    bugs = newBugs

    if tuple(bugs) in visited:
        break
    visited.add(tuple(bugs))

power = 0 
res = 0

for y in range(len(grid)):
    for x in range(len(grid[x])):
        if (x, y) in bugs:
           res += 2 ** power
        power += 1
print(res)
