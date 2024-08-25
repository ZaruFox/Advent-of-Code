with open("data.txt") as f:
    tree = [int(x) for x in f.readline().strip().split(" ")]

def dfs(i):
    numberOfNodes, numberOfMetadata = tree[i], tree[i+1]
    i += 2

    childNodeValues = []
    for _ in range(numberOfNodes):
        tmp = dfs(i)
        childNodeValues.append(tmp[0])
        i = tmp[1]

    totalMetadata = 0
    if numberOfNodes == 0:
        for _ in range(numberOfMetadata):
            totalMetadata += tree[i]
            i += 1
    else:
        for _ in range(numberOfMetadata):
            if tree[i] == 0 or tree[i]-1 >= numberOfNodes:
                i += 1
                continue

            totalMetadata += childNodeValues[tree[i]-1]
            i += 1

    return totalMetadata, i

print(dfs(0)[0])