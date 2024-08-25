from collections import defaultdict

bugs = set()

with open("data.txt") as f:
    grid = [x.strip() for x  in f.readlines()]

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "#":
            bugs.add((x, y, 0))

EDGES = {(1,2): [(0, y) for y in range(5)], (3,2): [(4, y) for y in range(5)], (2,1): [(x, 0) for x in range(5)], (2,3): [(x, 4) for x in range(5)]}

for i in range(200):
    adjBugs = defaultdict(int)

    for bugX, bugY, level in bugs:
        for adj in ((bugX, bugY+1), (bugX, bugY-1), (bugX+1, bugY), (bugX-1, bugY)):
            if not (0 <= adj[0] < len(grid[0]) and 0 <= adj[1] < len(grid)):
                if adj[0] == -1:
                    adjBugs[(1, 2, level-1)] += 1
                elif adj[0] == 5:
                    adjBugs[(3, 2, level-1)] += 1
                elif adj[1] == -1:
                    adjBugs[(2, 1, level-1)] += 1
                elif adj[1] == 5:
                    adjBugs[(2, 3, level-1)] += 1

            elif adj == (2, 2):
                for adj2 in EDGES[(bugX, bugY)]:
                    adjBugs[adj2 + (level+1,)] += 1

            else:
                adjBugs[adj + (level,)] += 1

    newBugs = set()
    for location, adjBugsCount in adjBugs.items():
        if location in bugs and adjBugsCount == 1:
            newBugs.add(location)
        elif location not in bugs and 1 <= adjBugsCount <= 2:
            newBugs.add(location)

    bugs = newBugs


print(len(bugs))