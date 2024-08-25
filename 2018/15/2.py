
from __future__ import annotations
from math import inf
from collections import deque

class Unit:
    def __init__(self, x: int, y: int, unitType: str, attackPower: int) -> None:
        self.attackPower = attackPower
        self.health = 200
        self.x = x
        self.y = y
        self.unitType = unitType

    def isEnemy(self, other: Unit) -> bool:
        return self.unitType != other.unitType
    
    def isDead(self):
        return self.health <= 0
    
    def attackEnemy(self, battle: Battle) -> None:
        adjEnemies = battle.getAdjEnemies(self)

        if adjEnemies:
            tmp = min(adjEnemies, key = lambda x: x.health)
            for enemy in adjEnemies:
                if enemy.health == tmp.health:
                    target = enemy
                    break

            target.health -= self.attackPower
            #print(f"{self.x},{self.y} ({self.health}) attacks {target.x}, {target.y} ({target.health})")

            if target.isDead():
                battle.grid[target.y][target.x] = "."
                #print(f"{target.x},{target.y} has died")

    def move(self, battle: Battle):
        
        if battle.getAdjEnemies(self):
            return 
        
        queue = deque([(newX, newY, newX, newY, 0) for newX, newY in battle.getAdjIndex(self.x, self.y) if battle.grid[newY][newX] == "."])
        visited = set([(newX, newY, newX, newY) for newX, newY in battle.getAdjIndex(self.x, self.y) if battle.grid[newY][newX] == "."]) 
        found = []
        minCost = inf
        done = False

        while queue and not done:
            curX, curY, oriX, oriY, cost = queue.popleft()

            for nextX, nextY in battle.getAdjIndex(curX, curY):
                val = battle.grid[nextY][nextX]
                if type(val) == Unit and val.isEnemy(self):
                    if cost == minCost or minCost == inf:
                        minCost = cost
                        found.append((curX, curY, oriX, oriY))
                    else:
                        done = True
                        break

                if val != "." or (nextX, nextY, oriX, oriY) in visited:
                    continue
                visited.add((nextX, nextY, oriX, oriY))

                queue.append((nextX, nextY, oriX, oriY, cost + 1))

        if found:
            target = sorted(found, key=lambda x:(x[1], x[0], x[3], x[2]))[0]
            battle.grid[self.y][self.x] = "."
            battle.grid[target[3]][target[2]] = self
            self.x = target[2]
            self.y = target[3]
        
    
    def __repr__(self):
        return f"{self.unitType} ({self.x} {self.y}): {self.health}"
    
class Battle:
    def __init__(self, data: list[list[str]], elfPower: int):
        self.grid = []

        for y in range(len(data)):
            row = list(data[y].strip())

            for x in range(len(row)):
                if row[x] in "EG":
                    row[x] = Unit(x, y, row[x], elfPower if row[x] == "E" else 3)
                
            self.grid.append(row)

    def getAdjIndex(self, x: int, y: int):
        return [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]
    
    def getAdjValue(self, x: int, y: int):
        return [self.grid[y1][x1] for x1, y1 in self.getAdjIndex(x, y)]
    
    def getAdjEnemies(self, current: Unit):
        return [x for x in self.getAdjValue(current.x, current.y) if type(x) == Unit and current.isEnemy(x)]

    def simulateRound(self, evlesCount):
        moveOrder: list[Unit] = []

        for row in self.grid:
            for tile in row:
                if type(tile) == Unit:
                    moveOrder.append(tile)

        for current in moveOrder:
            if current.isDead():
                continue

            if (x := self.checkOutcome(evlesCount)) != -2:
                return x

            # move if no enemy in range
            current.move(self)

            # attack if enemy in range
            current.attackEnemy(self)

        return -2

    def checkOutcome(self, evlesCount):
        allUnits = []
        for row in self.grid:
            for tile in row:
                if type(tile) == Unit:
                    allUnits.append(tile) 

        if all(x.unitType == "E" for x in allUnits) and len(allUnits) == evlesCount: 
            print([x for x in allUnits])
            return sum([x.health for x in allUnits])
        elif all(x.unitType == "E" for x in allUnits) or all(x.unitType == "G" for x in allUnits):
            return -1
        return -2
            

    def print(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if type(self.grid[y][x]) == Unit:
                    assert not self.grid[y][x].isDead()
                    print(self.grid[y][x].unitType, end="")
                else:
                    print(self.grid[y][x], end="")
            print()


with open("data.txt") as f:
    data = f.readlines()

evlesCount = 0
for line in data:
    evlesCount += line.count("E")

found = False
for power in range(4, 201):
    battle = Battle(data, power)
    numberOfRounds = 0
    while True:
        #battle.print()
        outcome = battle.simulateRound(evlesCount)
        #input()

        if outcome != -2:
            if outcome != -1:
                print(f"{outcome = }")
                print(f"{numberOfRounds = }")
                print(f"{power = }")
                print(outcome * (numberOfRounds))
                found = True
            break

        numberOfRounds += 1

    if found:
        break
