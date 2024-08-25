from copy import deepcopy

instructions = []

with open("data.txt") as f:
    for line in f:
        action, value = line.strip().split()
        instructions.append([action , int(value)])

def dfs(instructions):
    i = 0
    acc = 0
    visited = set()
    
    while i not in visited:
        if i == len(instructions):
            return acc
            
        visited.add(i)
    
        if instructions[i][0] == "acc":
            acc += instructions[i][1]
            i += 1
        elif instructions[i][0] == "jmp":
            i += instructions[i][1]
        else:
            i += 1
    
    return -1

for i in range(len(instructions)):
    editted = deepcopy(instructions)
    if instructions[i][0] == "jmp":
        editted[i][0] = "nop"
    if instructions[i][0] == "nop":
        editted[i][0] = "jmp"
        
    if (x := dfs(editted)) != -1:
        print(x)
        break
    