data = []

with open("5data.txt") as f:
    for line in f:
        data.append([tuple([int(y) for y in x.split(",")]) for x in line.strip().split(" -> ")])

res = 0
visited = set()
noCount = set()
for direction in data:
    if direction[0][0] == direction[1][0]:
        for i in range(min(direction[0][1], direction[1][1]), max(direction[0][1], direction[1][1])+1):
            if (direction[1][0], i) in visited and not (direction[1][0], i) in noCount:
                res += 1
                noCount.add((direction[1][0], i))

            else:
                visited.add((direction[1][0], i))
                
    
    elif direction[0][1] == direction[1][1]:
        for i in range(min(direction[0][0], direction[1][0]), max(direction[0][0], direction[1][0])+1):
            if (i, direction[1][1]) in visited and not (i, direction[1][1])  in noCount:
                res += 1
                noCount.add((i, direction[1][1]) )

            else:
                visited.add((i, direction[1][1]))

    #part 2
    else:
        xDiff = (direction[1][0] - direction[0][0]) // abs(direction[1][0] - direction[0][0])
        yDiff = (direction[1][1] - direction[0][1]) // abs(direction[1][1] - direction[0][1])

        print(direction, xDiff, yDiff)
        cur = direction[0]
        while cur != (direction[1][0] + xDiff, direction[1][1] + yDiff):
            if cur in visited and not cur in noCount:
                res += 1
                noCount.add(cur)

            else:
                visited.add(cur)

            cur = (cur[0] + xDiff, cur[1] + yDiff)

print(res)
        
        