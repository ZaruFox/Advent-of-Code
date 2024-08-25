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

prefixSum = [[0] for _ in range(n)]
for x in range(n):
    for y in range(n):
        prefixSum[x].append(prefixSum[x][-1] + powerCells[y][x])

maxTotal = -math.inf
res = (None, None, None)
for size in range(1, n+1):
    for y in range(n-size+1):
        curTotal = sum([prefixSum[newX][y+size]- prefixSum[newX][y] for newX in range(size)])
        if curTotal > maxTotal:
            maxTotal = curTotal
            res = (0, y, size)

        for x in range(1, n-size+1):
            curTotal -= prefixSum[x-1][y+size] - prefixSum[x-1][y]
            curTotal += prefixSum[x+size-1][y+size] - prefixSum[x+size-1][y]
            if curTotal > maxTotal:
                maxTotal = curTotal
                res = (x, y, size)

print(f"{res[0]},{res[1]},{res[2]}")

