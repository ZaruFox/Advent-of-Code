from collections import defaultdict, deque
import heapq
import sys

with open("data.txt") as f:
    grid = [list(line.strip("\n")) for line in f.readlines()]


portals = defaultdict(list)
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if "A" <= grid[y][x] <= "Z":

            if "A" <= grid[y][x+1] <= "Z":
                code = grid[y][x] + grid[y][x+1]
                if grid[y][x-1] == ".":
                    portals[code].append((x-1, y))
                else:
                    portals[code].append((x+2, y))
                grid[y][x+1] = " "

            else:
                code = grid[y][x] + grid[y+1][x]
                if grid[y-1][x] == ".":
                    portals[code].append((x, y-1))
                else:
                    portals[code].append((x, y+2))

                grid[y+1][x] = " "

            grid[y][x] = " "

start = portals.pop("AA")[0]
destination = portals.pop("ZZ")[0]

portalsCoords = {}
for coord1, coord2 in portals.values():
    portalsCoords[coord1] = coord2
    portalsCoords[coord2] = coord1

heap = [(0, 0, start)]
visited = {(start, 0)}

while heap:
    level, cost, cur = heapq.heappop(heap)  

    x, y = cur
    possibleNext = [((newX, newY), level) for newX, newY in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)] if grid[newY][newX] == "."]

    if cur in portalsCoords:
        if cur[0] == 2 or cur[0] == len(grid[0])-3 or cur[1] == 2 or cur[1] == len(grid)-3:
            if level != 0:
                possibleNext += [(portalsCoords[cur], level - 1)]
        else:
            possibleNext += [(portalsCoords[cur], level + 1)]
        
    for next in possibleNext:
        if next in visited:
            continue
        visited.add(next)

        nextCoords, nextLevel = next
        if nextCoords == destination:
            if nextLevel == 0:
                print(cost+1) 
                sys.exit()
            else:
                continue

        heapq.heappush(heap, (nextLevel, cost+1, nextCoords))



