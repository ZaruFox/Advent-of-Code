from itertools import cycle

cur = 0
visited = {0}
with open("data.txt") as f:
    for line in cycle(f):
        cur += int(line.strip())
        
        if cur in visited:
            print(cur)
            break
        visited.add(cur)