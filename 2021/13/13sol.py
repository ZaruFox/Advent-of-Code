holes = set()
instructions = []

with open("13data.txt") as f:
    for line in f:
        if line == "\n":
            break
        holes.add(tuple([int(x) for x in line.strip().split(",")]))

    for line in f:
        instructions.append(line.strip().split(" ")[-1].split("="))

    instructions = [[x[0], int(x[1])] for x in instructions]
    
dirToIndex = {"x":0, "y":1}
for i in range(len(instructions)):
    newHoles = set()
    dir, val = instructions[i]
    dir = dirToIndex[dir]
    
    for holePos in holes:
        holePos = list(holePos)
        if holePos[dir] > val:
            holePos[dir] = val - (holePos[dir] - val)

        newHoles.add(tuple(holePos))

    holes = newHoles


for y in range(6):
    for x in range(50):
        if (x,y) in holes:
            print('#', end="")
        else:
            print(".", end="")
    print()
            