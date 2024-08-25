import re
import copy

class Group:
    def __init__(self, side):
        self.side = side
        self.health = -1
        self.count = -1
        self.damage = -1
        self.initiative = -1

        self.damageType = ""
        self.immunity = []
        self.weaknesses = []

    def getEffPower(self):
        return self.damage * self.count
    
    def isDead(self):
        return self.count <= 0
    
    def isEnemy(self, other):
        return other.side != self.side
    
    def checkDamage(self, other):
        if self.damageType in other.immunity:
            return 0
        
        if self.damageType in other.weaknesses:
            return self.getEffPower() * 2
            
        return self.getEffPower()
    
    def dealDamage(self, other):
        damageDealt = self.checkDamage(other)
        other.count -= damageDealt // other.health


    def __repr__(self):
        return f"{self.side = }{self.health = }{self.count = }{self.damage = }{self.initiative = }{self.damageType = }{self.immunity = }{self.weaknesses = }\n"

def simulate(boost):
    with open("data.txt") as f:
        data = f.read().splitlines()

    groups: list[Group] = []
    for line in data:
        if line == "":
            continue

        if line == "Immune System:":
            side = 0
            continue

        if line == "Infection:":
            side = 1
            continue

        cur = Group(side)

        splitted = line.split(" ")
        cur.count, cur.health, cur.damage, cur.damageType, cur.initiative = int(splitted[0]), int(splitted[4]), int(splitted[-6]), splitted[-5], int(splitted[-1])

        if side == 0:
            cur.damage += boost

        info = re.search(r"\(.+\)", line)
        if info:
            info = info.group().strip("()").split("; ")
            
            for subInfo in info:
                if subInfo.startswith("weak to"):
                    cur.weaknesses = subInfo[8:].split(", ")
                else:
                    cur.immunity = subInfo[10:].split(", ")

        groups.append(cur)

    prevState = []
    while True:
        targetSelectionOrder = sorted(groups, key=lambda x: (x.getEffPower(), x.initiative), reverse=True)
        attackInfo = []
        beingAttacked = []

        for attackingGroup in targetSelectionOrder:
            candidates = [x for x in groups if (x not in beingAttacked) and (not x.isDead()) and (x.isEnemy(attackingGroup))]
            if not candidates:
                continue
            
            defendingGroup = max(candidates, key=lambda y: (attackingGroup.checkDamage(y), y.getEffPower(), y.initiative))
            damageDealt = attackingGroup.checkDamage(defendingGroup)

            if damageDealt == 0:
                continue

            attackInfo.append((attackingGroup, defendingGroup))
            beingAttacked.append(defendingGroup)

        attackInfo.sort(key=lambda x: x[0].initiative, reverse=True)

        for attacking, defending in attackInfo:
            if attacking.isDead():
                continue

            attacking.dealDamage(defending)

        groups = [x for x in groups if not x.isDead()]
        if all([x.side == 0 for x in groups]):
            return sum([x.count for x in groups])
        if all([x.side == 1 for x in groups]):
            return -sum([x.count for x in groups])
        if sum([x.count for x in groups]) == prevState:
            return 0
        prevState = sum([x.count for x in groups])
        
for boost in range(10000000):
    res = simulate(boost)
    if res > 0:
        print(res)
        break