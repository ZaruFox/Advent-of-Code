PATHS = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
grid = []

with open("data.txt") as f:
    for line in f:
        grid.append(line.strip())

res = 1
for xDelta, yDelta in PATHS:
    cur = [0, 0]
    numberOfTrees = 0
    
    while cur[1] < len(grid):
        if grid[cur[1]][cur[0]] == "#":
            numberOfTrees += 1
            
        cur[0] += xDelta
        cur[0] %= len(grid[0])
        cur[1] += yDelta

    res *= numberOfTrees

print(res)