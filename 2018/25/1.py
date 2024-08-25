with open("data.txt") as f:
    data = f.read().splitlines()

def findParent(disjoint, i):
    if disjoint[i] == -1:
        return i
    return findParent(disjoint, disjoint[i])

stars = [[int(x) for x in row.split(',')] for row in data]
disjoint = [-1] * len(stars)

for i in range(len(stars)):
    connected = []
    for j in range(i):
        if sum([abs(stars[i][k] - stars[j][k]) for k in range(4)]) <= 3:
            connected.append(j)

    for j in connected:
        parent = findParent(disjoint, j)
        if parent == i:
            continue
        disjoint[parent] = i

print(disjoint.count(-1))

        