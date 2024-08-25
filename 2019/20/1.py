from collections import defaultdict, deque

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

queue = deque([(start, 0)])
visited = {start}

while queue:
    cur, cost = queue.popleft()

    x, y = cur
    possibleNext = [(newX, newY) for newX, newY in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)] if grid[newY][newX] == "."]

    if cur in portalsCoords:
        possibleNext += [portalsCoords[cur]]

    for next in possibleNext:
        if next in visited:
            continue
        visited.add(next)

        if next == destination:
            print(cost+1)
            break

        queue.append((next, cost+1))




