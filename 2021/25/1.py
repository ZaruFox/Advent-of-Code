southCucumber = set()
eastCucumber = set()

with open("data.txt") as f:
    y = 0
    for line in f:
        for x in range(len(line)):
            if line[x] == ">":
                eastCucumber.add((x, y))
            elif line[x] == "v":
                southCucumber.add((x, y))
        y += 1

    maxX = len(line)
    maxY = y

moving = True
n = 0
while moving:
    moving = False
    n += 1
    
    newEast= set()
    for originalLocation in eastCucumber:
        nextLocation = ((originalLocation[0]+1) % maxX, originalLocation[1])   
        if nextLocation in eastCucumber or nextLocation in southCucumber:
            newEast.add(originalLocation)
        else:
            newEast.add(nextLocation)
            moving = True
    eastCucumber = newEast

    newSouth= set()
    for originalLocation in southCucumber:
        nextLocation = (originalLocation[0], (originalLocation[1]+1) % maxY)   
        if nextLocation in eastCucumber or nextLocation in southCucumber:
            newSouth.add(originalLocation)
        else:
            newSouth.add(nextLocation)
            moving = True
    southCucumber = newSouth

print(n)