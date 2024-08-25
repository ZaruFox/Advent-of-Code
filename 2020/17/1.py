from collections import defaultdict

ADJ = [(-1,-1,-1),(-1,-1,0),(-1,-1,1)
      ,(-1,0,-1),(-1,0,0),(-1,0,1)
      ,(-1,1,-1),(-1,1,0),(-1,1,1)
      ,(0,-1,-1),(0,-1,0),(0,-1,1)
      ,(0,0,-1),(0,0,1)
      ,(0,1,-1),(0,1,0),(0,1,1)
      ,(1,-1,-1),(1,-1,0),(1,-1,1)
      ,(1,0,-1),(1,0,0),(1,0,1)
      ,(1,1,-1),(1,1,0),(1,1,1)]

litCubes = set()
with open("data.txt") as f:
    y = 0
    for line in f:
        for x in range(len(line.strip())):
            if line[x] == "#":
                litCubes.add((x, y, 0))
        y += 1

for _ in range(6):
    adjActive = defaultdict(int)
    for x, y, z in litCubes:
        for xDiff, yDiff, zDiff in ADJ:
            adjActive[(x+xDiff, y+yDiff, z+zDiff)] += 1

    newLitCubes = set()
    for cube, n in adjActive.items():
        if (cube in litCubes and n in (2,3)) or (cube not in litCubes and n == 3):
            newLitCubes.add(cube)
    litCubes = newLitCubes

print(len(litCubes))
            