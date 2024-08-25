VALIDMOVES = {"|": [(0, -1), (0, 1)], "-": [(-1, 0), (1, 0)],
             "F": [(0, 1), (1, 0)], "L": [(0, -1), (1, 0)],
             "J": [(0, -1), (-1, 0)], "7": [(0, 1), (-1, 0)]}
map = []
with open("data.txt") as f:
    y = 0
    for line in f:
        if "S" in line:
            start = (line.find("S"), y)
            line = line.replace("S", "|")
        map.append(list(line.strip()))
        y += 1

steps = 0
cur = start
prev = None
while True:
    for diff in VALIDMOVES[map[cur[1]][cur[0]]]:
        next = (diff[0] + cur[0], diff[1] + cur[1])
        if next == prev:
            continue
        prev, cur = cur, next
        break
        

    steps += 1
    if cur == start:
        print(steps // 2)
        break