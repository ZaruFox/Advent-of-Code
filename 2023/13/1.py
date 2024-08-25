def findHorizontal(map):
    for i in range(1, len(map)):
        l = i-1
        r = i
        valid = True
        
        while l >= 0 and r < len(map):
            if map[l] != map[r]:
                valid = False
                break

            l -= 1
            r += 1

        if valid:
            return i

    return 0


def transpose(map):
    return [[map[y][x] for y in range(len(map))] for x in range(len(map[0]))]
    
data = []

with open("data.txt") as f:
    map = []
    for line in f:
        if line == "\n":
            data.append(map)
            map = []
        else:
            map.append(line.strip())
    data.append(map)
res = 0
for map in data:
    res += findHorizontal(map)*100
    map = transpose(map)
    res += findHorizontal(map)

print(res)