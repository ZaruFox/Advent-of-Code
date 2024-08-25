import sys
sys.setrecursionlimit(1500)

map = []
with open("data.txt") as f:
    for line in f:
        map.append(line.strip())

def dfs(x, y, map, visited):
    counter = 0
    prev = None
    while True:
        if x == len(map[0]) - 2 and y == len(map) - 1:
            return counter 
            
        possibleMoves = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]
        if map[y][x] == ">":
            possibleMoves = [(x+1, y)]
        elif map[y][x] == "<":
            possibleMoves = [(x-1, y)]
        elif map[y][x] == "^":
            possibleMoves = [(x, y-1)]
        elif map[y][x] == "v":
            possibleMoves = [(x, y+1)]
    
        validMoves = []
        for nextMove in possibleMoves:
            if nextMove == prev or nextMove in visited or map[nextMove[1]][nextMove[0]] == "#":
                continue
    
            validMoves.append(nextMove)

        
        if len(validMoves) == 1:
            prev = (x,y)
            x, y = validMoves[0]
            counter += 1
        else:
            maximum = 0
            for move in validMoves:
                maximum = max(maximum, dfs(move[0], move[1], map, set([(x, y)]) | visited) + counter + 1)
            return maximum

print(dfs(1, 0, map, set()))