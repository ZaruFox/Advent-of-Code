data = []
pos = [0, 0]
RULES = {"forward": [0, 1], "down": [1, 1], "up": [1,-1]}

with open("2data.txt") as f:
    for line in f:
        data.append(line.strip().split(" "))

data = [[x[0], int(x[1])] for x in data]

for dir in data:
    pos[RULES[dir[0]][0]] += dir[1] * RULES[dir[0]][1]

print(pos[0] * pos[1])



#part 2
data = []
pos = [0, 0, 0]
RULES = {"forward": [0, 1], "down": [2, 1], "up": [2,-1]}

with open("2data.txt") as f:
    for line in f:
        data.append(line.strip().split(" "))

data = [[x[0], int(x[1])] for x in data]

for dir in data:
    pos[RULES[dir[0]][0]] += dir[1] * RULES[dir[0]][1]
    if dir[0] == "forward":
        pos[1] += dir[1] * pos[2]

print(pos[0] * pos[1])