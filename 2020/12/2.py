operations = []

with open("data.txt") as f:
    for line in f:
        operations.append((line[0], int(line.strip()[1:])))


waypointX = -10
waypointY = -1
shipX = 0
shipY = 0
for action, value in operations:
    if action == "F":
        shipX += waypointX * value
        shipY += waypointY * value
    elif action == "N":
        waypointY -= value
    elif action == "S":
        waypointY += value
    elif action == "W":
        waypointX += value
    elif action == "E":
        waypointX -= value
    elif action == "L":
        for _ in range(value // 90):
            waypointX, waypointY = -waypointY, waypointX
    elif action == "R":
        for _ in range(value // 90):
            waypointX, waypointY = waypointY, -waypointX

print(abs(shipX) + abs(shipY))