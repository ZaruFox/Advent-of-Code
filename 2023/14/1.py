map = []

with open("data.txt") as f:
    for line in f:
        map.append(line.strip())

res = 0
n = len(map)

for x in range(len(map[0])):
    destination = 0
    for y in range(n):
        if map[y][x] == "O":
            res += n - destination
            destination += 1
        elif map[y][x] == "#":
            destination = y + 1

print(res)