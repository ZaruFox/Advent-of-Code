numberOfTrees = 0
with open("data.txt") as f:
    xPos = 0
    for line in f:
        if line[xPos] == "#":
            numberOfTrees += 1

        xPos = (xPos + 3) % (len(line)-1)

print(numberOfTrees)