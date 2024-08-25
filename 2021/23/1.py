import functools
import math

STEPCOST = {"A": 1, "B": 10, "C": 100, "D": 1000}
ROOMINDEX = {"A": 1, "B": 2, "C": 3, "D": 4}

def replaceIndex(x, i, r):
    x = list(x)
    x[i] = r
    return tuple(x)
    
@functools.cache
def dp(rooms, corridor):
    if all([value == (key, key) for key, value in rooms]):
        return 0
        
    res = math.inf
    rooms = dict(rooms)

    for i in range(7):
        if corridor[i] == ".":
            continue

        aphid = corridor[i]
        if rooms[aphid] == () or all([aphid == x for x in rooms[corridor[i]]]):
            newRooms = rooms.copy()
            newRooms[aphid] = (aphid,) + rooms[aphid]
            newRooms = tuple(newRooms.items())

            if i > ROOMINDEX[aphid] and all([x == "." for x in corridor[ROOMINDEX[aphid]+1:i]]):
                numberOfSteps = 3 - len(rooms[aphid]) + (i-1-ROOMINDEX[aphid]) * 2
                if i == 6:
                    numberOfSteps -= 1
                    
                return dp(newRooms, replaceIndex(corridor, i, ".")) + STEPCOST[aphid] * numberOfSteps

            elif i <= ROOMINDEX[aphid] and all([x == "." for x in corridor[i+1:ROOMINDEX[aphid]+1]]):
                numberOfSteps = 3 - len(rooms[aphid]) + (ROOMINDEX[aphid]-i) * 2
                if i == 0:
                    numberOfSteps -= 1
    
                return dp(newRooms, replaceIndex(corridor, i, ".")) + STEPCOST[aphid] * numberOfSteps

    
    for key, value in rooms.items():
        if value == () or all([key == x for x in value]):
            continue

        aphid = value[0]
        newRooms = rooms.copy()
        newRooms[key] = value[1:]
        newRooms = tuple(newRooms.items())

        cost = STEPCOST[aphid]*2 if len(value) == 2 else STEPCOST[aphid]*3
        for i in range(ROOMINDEX[key]+1, 7):
            if corridor[i] != ".":
                break

            res = min(res, dp(newRooms, replaceIndex(corridor, i, aphid))+cost)
            if i == 5:
                cost += STEPCOST[aphid]
            else:
                cost += STEPCOST[aphid]*2

        cost = STEPCOST[aphid]*2 if len(value) == 2 else STEPCOST[aphid]*3
        for i in range(ROOMINDEX[key], -1, -1):
            if corridor[i] != ".":
                break
    
            res = min(res, dp(newRooms, replaceIndex(corridor, i, aphid))+cost)
            if i == 1:
                cost += STEPCOST[aphid]
            else:
                cost += STEPCOST[aphid]*2

    return res

        

with open("test.txt") as f:
    data = f.readlines()

holes = {"A": [], "B": [], "C": [], "D": []}

for i in range(2, 4):
    holes["A"].append(data[i][3])
    holes["B"].append(data[i][5])
    holes["C"].append(data[i][7])
    holes["D"].append(data[i][9])

rooms = tuple({key: tuple(value) for key, value in holes.items()}.items())
corridor = (".") * 7

print(dp(rooms, corridor))

