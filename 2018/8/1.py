with open("data.txt") as f:
    tree = [int(x) for x in f.readline().strip().split(" ")]

def dfs(i):
    numberOfNodes, numberOfMetadata = tree[i], tree[i+1]
    totalMetadata = 0
    i += 2

    for _ in range(numberOfNodes):
        tmp = dfs(i)
        totalMetadata += tmp[0]
        i = tmp[1]

    for _ in range(numberOfMetadata):
        totalMetadata += tree[i]
        i += 1

    return totalMetadata, i

print(dfs(0)[0])