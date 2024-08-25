depth = 11109
target = (9,731)

erosionLevel = [[0] * (target[0]+1) for _ in range(target[1]+1)]

for y in range(len(erosionLevel)):
    for x in range(len(erosionLevel[0])):
        if (x, y) == (0, 0) or (x, y) == target:
            index = 0
        elif y == 0:
            index = x * 16807
        elif x == 0:
            index = y * 48271
        else:
            index = erosionLevel[y][x-1] * erosionLevel[y-1][x]

        erosionLevel[y][x] = (index + depth) % 20183

groundType = [[level % 3 for level in row] for row in erosionLevel]
print(sum([sum(row) for row in groundType]))

