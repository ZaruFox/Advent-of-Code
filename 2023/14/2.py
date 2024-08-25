
def push(map, direction):
    n = len(map)
    m = len(map[0])
    
    if direction == "N":
        for x in range(m):
            destination = 0
            for y in range(n):
                if map[y][x] == "O":
                    map[y][x] = "."
                    map[destination][x] = "O"
                    destination += 1
                elif map[y][x] == "#":
                    destination = y + 1
    elif direction == "S":
        for x in range(m):
            destination = n-1
            for y in range(n-1,-1,-1):
                if map[y][x] == "O":
                    map[y][x] = "."
                    map[destination][x] = "O"
                    destination -= 1
                elif map[y][x] == "#":
                    destination = y - 1

    elif direction == "W":
        for y in range(n):
            destination = 0
            for x in range(m):
                if map[y][x] == "O":
                    map[y][x] = "."
                    map[y][destination] = "O"
                    destination += 1
                elif map[y][x] == "#":
                    destination = x + 1

    elif direction == "E":
        for y in range(n):
            destination = m-1
            for x in range(m-1,-1,-1):
                if map[y][x] == "O":
                    map[y][x] = "."
                    map[y][destination] = "O"
                    destination -= 1
                elif map[y][x] == "#":
                    destination = x - 1


def calcPoints(map):
    res = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "O":
                res += len(map)-y

    return res
                
map = []

with open("data.txt") as f:
    for line in f:
        map.append(list(line.strip()))

n = len(map)
m = len(map[0])
prev = []
counter = 0

for i in range(1000):
    push(map, "N")
    push(map, "W")
    push(map, "S")
    push(map, "E")
    
    # points = calcPoints(map)
    
    # if points in prev:
        
    #     print(i)
    #     print(points)
    #     counter += 1
    #     if counter == 16:
    #         break

    # prev.append(points)
    
    #print("\n".join(["".join(x) for x in map]))
    # cycle len 7
    # second loop starts at 100 cycle
    # loop starts at 94,
    # 
print(calcPoints(map))