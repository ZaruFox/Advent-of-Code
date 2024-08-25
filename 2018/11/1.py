import math

with open("data.txt") as f:
    serialNumber = int(f.readline().strip())

n = 300
powerCells = [[0] * n for _ in range(n)]

for y in range(n):
    for x in range(n):
        rackID = x + 10
        powerLevel = (rackID * y + serialNumber) * rackID
        powerLevel = ((powerLevel // 100) % 10) - 5
        powerCells[y][x] = powerLevel

maxTotal = -math.inf
res = (None, None)

for y in range(n-2):
    curTotal = sum([powerCells[newY][0] + powerCells[newY][1] + powerCells[newY][2] for newY in range(y, y+3)])
    if curTotal > maxTotal:
        maxTotal = curTotal
        res = (0, y)

    for x in range(1, n-2):
        curTotal -= sum([powerCells[newY][x-1] for newY in range(y, y+3)])
        curTotal += sum([powerCells[newY][x+2] for newY in range(y, y+3)])

        if curTotal > maxTotal:
            maxTotal = curTotal
            res = (x, y)

print(res)

