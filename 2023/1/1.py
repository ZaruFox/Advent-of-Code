res = 0
with open("data.txt") as f:
    for line in f:
        for i in range(len(line)):
            if line[i].isdigit():
                res += int(line[i]) * 10
                break

        for j in range(len(line)-1,-1,-1):
            if line[j].isdigit():
                res += int(line[j])
                break
        
print(res)