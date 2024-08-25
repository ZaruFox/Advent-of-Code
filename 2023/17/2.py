from heapq import heappop, heappush
import math

def in_range(x, y, data):
    return (0 <= x < len(data[0])) and (0 <= y < len(data))

data = []
with open("data.txt") as f:
    for line in f:
        data.append([int(x) for x in list(line.strip())])

heap = [(0, 0, 0, None)]
visitedHorizontal = [[math.inf]*len(data[0]) for i in range(len(data))]
visitedVertical = [[math.inf]*len(data[0]) for i in range(len(data))]
visitedHorizontal[0][0] = 0
visitedVertical[0][0] = 0

while heap:
    cost, x, y, prevDirection = heappop(heap)
    if x == len(data[0])-1 and y == len(data)-1:
        print(cost)
        break


    if prevDirection != "horizontal":
        for xDiff in range(-10, 11):
            newX = x+xDiff
            if abs(xDiff) < 4 or not in_range(newX, y, data):
                continue

            newCost = sum(data[y][min(newX, x): max(newX, x)+1]) - data[y][x] + cost
            if newCost < visitedHorizontal[y][newX]:
                heappush(heap, (newCost, newX, y, "horizontal"))
                visitedHorizontal[y][newX] = newCost

    if prevDirection != "vertical":
        for yDiff in range(-10, 11):
            newY = y+yDiff
            if abs(yDiff) < 4 or not in_range(x, newY, data):
                continue

            newCost = sum([data[z][x] for z in range(min(newY, y), max(newY, y)+1)]) - data[y][x] + cost
            if newCost < visitedVertical[newY][x]:
                heappush(heap, (newCost, x, newY, "vertical"))
                visitedVertical[newY][x] = newCost


