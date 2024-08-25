from collections import defaultdict, deque

DIRECTIONS = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0)}

with open("data.txt") as f:
    regex = f.readline().strip("^$\n")

edges = defaultdict(set)

def dfs(i, positions):
    while i < len(regex):
        if regex[i] in "NWES":
            positions = list(positions)
            if len(positions) != 1:
                print(positions)
                print(regex[i-100:i+1])
                exit()
            for j in range(len(positions)):
                position = positions[j]

                newPosition = (position[0] + DIRECTIONS[regex[i]][0], position[1] + DIRECTIONS[regex[i]][1])
                edges[position].add(newPosition)
                edges[newPosition].add(position)

                positions[j] = newPosition
            i += 1
            positions = tuple(positions)

        elif regex[i] == "(":
            newPositions = set()

            i, x = dfs(i+1, positions)
            newPositions |= set(x)

            while regex[i-1] == "|":
                i, x = dfs(i, positions)
                newPositions |= set(x)

            positions = tuple(newPositions)


        elif regex[i] in ")|":
            return i + 1, positions
        
    return i

# generate adjDict    
dfs(0, ((0, 0),))

#bfs
queue = deque([((0, 0), 0)])
visited = {(0, 0)}
res = 0

while queue:
    pos, cost = queue.popleft()
    res = max(res, cost)

    for nextPos in edges[pos]:
        if nextPos in visited:
            continue
        visited.add(nextPos)

        queue.append((nextPos, cost + 1))

print(res)