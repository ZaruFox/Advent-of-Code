import math

reactions = {}

with open("data.txt") as f:
    for line in f:
        reactants = []
        line = line.strip().split()
        for i in range(0, len(line)-3, 2):
            reactants.append((line[i+1].strip(","), int(line[i])))

        reactions[line[-1]] = (int(line[-2]), reactants)

chemicals = {"FUEL": 1}
leftoverChemicals = {}
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

print(oreCount)