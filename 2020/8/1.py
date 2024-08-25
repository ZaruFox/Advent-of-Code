instructions = []

with open("data.txt") as f:
    for line in f:
        action, value = line.strip().split()
        instructions.append((action , int(value)))

i = 0
acc = 0
visited = set()

while i not in visited:
    visited.add(i)
    
    if instructions[i][0] == "acc":
        acc += instructions[i][1]
        i += 1
    elif instructions[i][0] == "jmp":
        i += instructions[i][1]
    else:
        i += 1

print(acc)