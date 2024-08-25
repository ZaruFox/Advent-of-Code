import math
import bisect

reactions = {}

with open("data.txt") as f:
    for line in f:
        reactants = []
        line = line.strip().split()
        for i in range(0, len(line)-3, 2):
            reactants.append((line[i+1].strip(","), int(line[i])))

        reactions[line[-1]] = (int(line[-2]), reactants)

def calcOreNeeded(fuelCount, leftoverChemicals = {}):
    chemicals = {"FUEL": fuelCount}
    leftoverChemicals = leftoverChemicals.copy()
    oreCount = 0
    
    while chemicals:
        cur = list(chemicals.keys())[0]
        quantityNeeded = chemicals.pop(cur)
        quantityMade, reactants = reactions[cur]
    
        if cur in leftoverChemicals:
            if quantityNeeded > leftoverChemicals[cur]:
                quantityNeeded -= leftoverChemicals[cur]
                leftoverChemicals[cur] = 0
            else:
                leftoverChemicals[cur] -= quantityNeeded
                continue
    
        reactionCount = math.ceil(quantityNeeded / quantityMade)
        leftoverChemicals[cur] = reactionCount*quantityMade - quantityNeeded
    
        for reactant, quantity in reactants:
            totalQuantity = quantity*reactionCount
            if reactant == "ORE":
                oreCount += totalQuantity
            elif reactant in chemicals:
                chemicals[reactant] += totalQuantity
            else:
                chemicals[reactant] = totalQuantity


    return oreCount
    
oreNeeded = calcOreNeeded(1)
fuelMade = 1_000_000_000_000 // oreNeeded

print(bisect.bisect_left(range(fuelMade, fuelMade + 1000000), 1_000_000_000_000, key = calcOreNeeded) + fuelMade-1)