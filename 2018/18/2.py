from collections import defaultdict

tree = set()
lumberyard = set()

with open("data.txt") as f:
    data = f.read().splitlines()

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "|":
            tree.add((x, y))
        elif data[y][x] == "#":
            lumberyard.add((x, y))

visited = {}
instances = []

for cycle in range(1000000000):
    treeCount = defaultdict(int)
    lumberCount = defaultdict(int)

    hashed = (tuple(tree), tuple(lumberyard))
    if hashed in visited:
        cycleStart = visited[hashed]
        cycleLength = cycle - cycleStart
        break

    visited[hashed] = cycle
    instances.append(hashed)

    for x, y in tree:
        for adj in [(x+1,y-1), (x, y-1), (x-1, y-1), (x+1, y), (x-1, y), (x+1, y+1), (x, y+1), (x-1, y+1)]:
            treeCount[adj] += 1

    for x, y in lumberyard:
        for adj in [(x+1,y-1), (x, y-1), (x-1, y-1), (x+1, y), (x-1, y), (x+1, y+1), (x, y+1), (x-1, y+1)]:
            lumberCount[adj] += 1

    for x, y in treeCount.keys() | lumberCount.keys() | tree | lumberyard:
        if not (0 <= x < len(data[0]) and 0 <= y < len(data)):
            continue

        if ((x, y) not in tree and (x, y) not in lumberyard) and treeCount[(x, y)] >= 3:
            tree.add((x, y))

        elif (x, y) in tree and lumberCount[(x, y)] >= 3:
            tree.discard((x, y))
            lumberyard.add((x, y))

        elif (x, y) in lumberyard and not (treeCount[(x, y)] >= 1 and lumberCount[(x, y)] >= 1):
            lumberyard.discard((x, y))

n = 1000000000
n -= cycleStart
n %= cycleLength
print(len(instances[n+cycleStart][0]) * len(instances[n+cycleStart][1]))
