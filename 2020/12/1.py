DIRECTIONS = ["N", "E", "S", "W"]
operations = []

with open("data.txt") as f:
    for line in f:
        operations.append((line[0], int(line.strip()[1:])))


shipDirection = 1
shipX = 0
shipY = 0
for action, value in operations:
    if action == "F":
        action = DIRECTIONS[shipDirection]
    
    if action == "N":
        shipY -= value
    elif action == "S":
        shipY += value
    elif action == "W":
        shipX += value
    elif action == "E":
        shipX -= value
    elif action == "L":
        shipDirection -= (value // 90)
        shipDirection %= 4
    elif action == "R":
        shipDirection += (value // 90)
        shipDirection %= 4

print(abs(shipX) + abs(shipY))