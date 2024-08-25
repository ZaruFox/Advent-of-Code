import re
import copy

# 286332 167624

moons = []
with open("data.txt") as f:
    for line in f:
        x, y, z = re.split(r", [yz]=", line.strip("<>x=\n")) 
        moons.append([[int(x),int(y),int(z)], [0,0,0]])

original = copy.deepcopy(moons)
prev = set()
l = None
steps = 0
while True:
    if steps % 50000 == 0:
        print(steps)

    x = 2
    tmp = (moons[0][0][x], moons[0][1][x], moons[1][0][x], moons[1][1][x], moons[2][0][x], moons[2][1][x], moons[3][0][x], moons[3][1][x])
    if tmp == l:
        print(steps)
    if l == None and tmp in prev:
        print(steps)
        l = tmp
    prev.add(tmp)
        
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

    steps += 1
    if moons == original:
        print(steps)
        break
