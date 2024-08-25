from collections import Counter

DIRECTIONS = [1, 1j, -1, -1j]
START = {">": 1, "<":-1, "^":-1j, "v":1j}
TURNS = {"/": {1:-1j, -1j:1, 1j:-1, -1:1j}, "\\": {1:1j, 1j:1, -1:-1j, -1j:-1}}
DESICION = [-1, 0, 1]

trains = []
grid = []
with open("data.txt") as f:
    lines = f.readlines()

    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip("\n")):
            if char in START:
                trains.append([complex(x, y), START[char], 0])
        grid.append(line.strip("\n"))

while len(trains) != 1:
    i = 0
    trains.sort(key = lambda x: (x[0].imag, x[0].real))
    while i < len(trains):
        trains[i][0] += trains[i][1]

        pos, direction, state = trains[i]
        newLocation = grid[int(pos.imag)][int(pos.real)]
        if newLocation in TURNS:
            trains[i][1] = TURNS[newLocation][direction]
        elif newLocation == "+":
            trains[i][1] = DIRECTIONS[(DIRECTIONS.index(direction) + DESICION[state]) % 4]

            trains[i][2] += 1
            trains[i][2] %= 3

        allPositions = [x[0] for x in trains]
        if len(set(allPositions)) != len(trains):
            crashLocation = [x for x, count in Counter(allPositions).items() if count >= 2][0]
            j = 0
            while j < len(trains):
                if trains[j][0] == crashLocation:
                    trains.pop(j)
                    if i >= j:
                        i -= 1
                else:
                    j += 1

        i += 1


lastTrain = trains[0][0]
print(f"{lastTrain.real:.0f},{lastTrain.imag:.0f}")