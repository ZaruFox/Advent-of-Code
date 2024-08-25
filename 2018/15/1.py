from __future__ import annotations
from collections import deque

class Unit:
    def __init__(self, x: int, y: int, unitType: str) -> None:
        self.attackPower = 3
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
            target = sorted(adjEnemies, key=lambda x: x.health)[0]

            target.health -= self.attackPower
            #print(f"{self.x},{self.y} ({self.health}) attacks {target.x}, {target.y} ({target.health})")

            if target.isDead():
                battle.grid[target.y][target.x] = "."
                #print(f"{target.x},{target.y} has died")

    def move(self, battle: Battle):
        if battle.getAdjEnemies(self):
            return 
        
        queue = deque([(newX, newY, newX, newY) for newX, newY in battle.getAdjIndex(self.x, self.y) if battle.grid[newY][newX] == "."])
        visited = set(battle.getAdjIndex(self.x, self.y)) 
        visited.add((self.x, self.y))
        found = None

        while found is None and queue:
            curX, curY, originalX, originalY = queue.popleft()

            for nextX, nextY in battle.getAdjIndex(curX, curY):
                val = battle.grid[nextY][nextX]
                if type(val) == Unit and val.isEnemy(self):
                    found = (originalX, originalY)
                    break

                if val != "." or (nextX, nextY) in visited:
                    continue
                visited.add((nextX, nextY))

                queue.append((nextX, nextY, originalX, originalY))

        if found is not None:
            battle.grid[self.y][self.x] = "."
            battle.grid[found[1]][found[0]] = self
            self.x = found[0]
            self.y = found[1]
        
    
    def __repr__(self):
        return f"{self.unitType}: {self.health}"
    
class Battle:
    def __init__(self, data: list[list[str]]):
        self.grid = []

        for y in range(len(data)):
            row = list(data[y].strip())

            for x in range(len(row)):
                if row[x] in "EG":
                    row[x] = Unit(x, y, row[x])
                
            self.grid.append(row)

    def getAdjIndex(self, x: int, y: int):
        return [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]
    
    def getAdjValue(self, x: int, y: int):
        return [self.grid[y1][x1] for x1, y1 in self.getAdjIndex(x, y)]
    
    def getAdjEnemies(self, current: Unit):
        return [x for x in self.getAdjValue(current.x, current.y) if type(x) == Unit and current.isEnemy(x)]

    def simulateRound(self):
        moveOrder: list[Unit] = []

        for row in self.grid:
            for tile in row:
                if type(tile) == Unit:
                    moveOrder.append(tile)

        for current in moveOrder:
            if current.isDead():
                continue

            # move if no enemy in range
            current.move(self)

            # attack if enemy in range
            current.attackEnemy(self)

    def checkOutcome(self) -> int:
        allUnits = []
        for row in self.grid:
            for tile in row:
                if type(tile) == Unit:
                    allUnits.append(tile) 

        if all(x.unitType == "E" for x in allUnits) or all(x.unitType == "G" for x in allUnits):
            return sum([x.health for x in allUnits])
        return -1  
            

    def print(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if type(self.grid[y][x]) == Unit:
                    print(self.grid[y][x].unitType, end="")
                else:
                    print(self.grid[y][x], end="")
            print()


with open("data.txt") as f:
    data = f.readlines()

battle = Battle(data)
numberOfRounds = 0
while True:
    #battle.print()
    battle.simulateRound()
    #input()

    outcome = battle.checkOutcome()
    if outcome != -1:
        print(f"{outcome = }")
        print(f"{numberOfRounds = }")
        print(outcome * numberOfRounds)
        break

    numberOfRounds += 1
