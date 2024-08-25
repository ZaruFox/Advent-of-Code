"""
x = mod of z
z //= (26 or 1)
if (x) + (constant1) != input:
   z *= 26
   z += input + (constant2)

"""

from functools import cache

data = []
with open("data.txt") as f:
    for line in f:
        if line == "inp w\n":
            data.append([])
        else:
            data[-1].append(line.strip().split())

parsedData = []
for i in range(len(data)):
    parsedData.append([int(data[i][3][2]), int(data[i][4][2]), int(data[i][14][2])])

print(parsedData)
    
@cache
def dp(i, z):
    if i == len(data):
        return "" if z == 0 else -1

    x = (z % 26) + parsedData[i][1]
    originalZ = z // parsedData[i][0]
    for w in range(9, 0, -1):
        z = originalZ
        if x != w:
           z *= 26
           z += w + parsedData[i][2]
        
        tmp = dp(i+1, z)
        if tmp != -1:
            return str(w) + tmp

    return -1

print(dp(0, 0))