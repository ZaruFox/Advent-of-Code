import re

def getEnergy(x):
    return sum([abs(y) for y in x])
    
moons = []
with open("data.txt") as f:
    for line in f:
        x, y, z = re.split(r", [yz]=", line.strip("<>x=\n")) 
        moons.append([[int(x),int(y),int(z)], [0,0,0]])

for step in range(1000):
    
    for i in range(4):
        for j in range(i+1, 4):
            for direction in range(3):
                if moons[i][0][direction] > moons[j][0][direction]:
                    moons[i][1][direction] -= 1
                    moons[j][1][direction] += 1
                elif moons[i][0][direction] < moons[j][0][direction]:
                    moons[i][1][direction] += 1
                    moons[j][1][direction] -= 1

    for i in range(4):
        for direction in range(3):
            moons[i][0][direction] += moons[i][1][direction]

res = 0    
for moon in moons:
    res += getEnergy(moon[0]) * getEnergy(moon[1])
print(res)