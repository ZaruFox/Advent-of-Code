hailstones = []

with open("data.txt") as f:
    for line in f:
        location, velocity = [[int(y) for y in x.split(", ")] for x in line.strip().split(" @ ")]

        gradient = velocity[1] / velocity[0]
        constant = location[1] - (gradient * location[0])
        hailstones.append([constant, gradient, location, velocity])

res = 0
validRange = (200000000000000, 400000000000000)
for i in range(len(hailstones)):
    for j in range(i+1, len(hailstones)):
        if hailstones[i][1] == hailstones[j][1]:
            continue
            
        xIntersect = (hailstones[j][0] - hailstones[i][0]) / (hailstones[i][1] - hailstones[j][1])
        yIntersect = hailstones[i][1] * xIntersect + hailstones[i][0]

        valid = validRange[0] <= xIntersect <= validRange[1] and validRange[0] <= yIntersect <= validRange[1]

        for stone in (hailstones[i], hailstones[j]):
            if (stone[3][0] < 0 and xIntersect > stone[2][0]) or (stone[3][0] > 0 and xIntersect < stone[2][0]) or (stone[3][1] < 0 and yIntersect > stone[2][1]) or (stone[3][1] > 0 and yIntersect < stone[2][1]):
                valid = False

        if valid:
            res += 1
                    
print(res)