litPixels = set()
with open("data.txt") as f:
    hashmap = f.readline().strip()
    f.readline()
    y = 0
    for line in f:
        for x in range(len(line)):
            if line[x] == "#":
                litPixels.add((x, y))
        y += 1

for i in range(50):
    newLitPixels = set()
    visited = set()
    for litPixel in litPixels:
        x1, y1 = litPixel
        for x, y in [(x1-1, y1-1), (x1, y1-1), (x1+1,y1-1), (x1-1, y1), (x1, y1), (x1+1, y1), (x1-1, y1+1), (x1, y1+1), (x1+1, y1+1)]:
            if (x, y) in visited:
                continue

            total = 0
            for value, checkPos in enumerate([(x-1, y-1), (x, y-1), (x+1,y-1), (x-1, y), (x, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]):
                if (i % 2 == 0 and checkPos in litPixels) or (i % 2 == 1 and not checkPos in litPixels):
                    total += 2 ** (8-value)

            if (i % 2 == 0 and hashmap[total] == ".") or (i % 2 == 1 and hashmap[total] == "#"):
                newLitPixels.add((x, y))
            visited.add((x, y))

    litPixels = newLitPixels            

print(len(litPixels))