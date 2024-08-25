from math import inf

with open("data.txt") as f:
    wire1 = [(x[0], int(x[1:])) for x in f.readline().strip().split(",")]
    wire2 = [(x[0], int(x[1:])) for x in f.readline().strip().split(",")]

wirePath = set()
cur = [0,0]
for direction, count in wire1:
    for _ in range(count):
        if direction == "U":
            cur[1] -= 1
        elif direction == "D":
            cur[1] += 1
        elif direction == "L":
            cur[0] -= 1
        elif direction == "R":
            cur[0] += 1
        else:
            raise Exception("a")
        wirePath.add(tuple(cur))

res = inf
cur = [0, 0]
for direction, count in wire2:
    for _ in range(count):
        if direction == "U":
            cur[1] -= 1
        elif direction == "D":
            cur[1] += 1
        elif direction == "L":
            cur[0] -= 1
        elif direction == "R":
            cur[0] += 1
        else:
            raise Exception("a")
            
        if tuple(cur) in wirePath:
            res = min(abs(cur[0])+abs(cur[1]), res)
print(res)