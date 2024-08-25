corners = []
cur = [0, 0]
res = 0

with open("data.txt") as f:
    for line in f:
        lineData = line.strip().split()[-1]
        steps, direction = int(lineData[2:7], 16), int(lineData[7])

        if direction == 0:
            cur[0] += steps
        elif direction == 1:
            cur[1] += steps
        elif direction == 2:
            cur[0] -= steps
        else:
            cur[1] -= steps

        res += steps
        corners.append(cur.copy())

for i in range(len(corners)-1):
    res += corners[i][0] * corners[i+1][1]
    res -= corners[i][1] * corners[i+1][0]
    
print(res // 2 + 1)

      