constraints = {}
myTicket = []
otherTickets = []
with open("data.txt") as f:
    for line in f:
        if line == "\n":
            break
        label, ranges = line.strip().split(": ")
        constraints[label] = [[int(y) for y in x.split("-")] for x in ranges.split(" or ")]

    f.readline()
    myTicket = [int(x) for x in f.readline().strip().split(",")]
    f.readline()
    f.readline()

    for line in f:
        otherTickets.append([int(x) for x in line.strip().split(",")])

res = 0
validTickets = []
for ticket in otherTickets:
    ticketValid = True
    for value in ticket:
        valid = False
        for range1, range2 in constraints.values():
            if range1[0] <= value <= range1[1] or range2[0] <= value <= range2[1]:
                valid = True
                break

        if not valid:
            ticketValid = False
            break

    if ticketValid:
        validTickets.append(ticket)

constraintToColumn = {x:None for x in constraints.keys()}
while any(x == None for x in constraintToColumn.values()):
    for column in range(len(validTickets[0])):
        validConstraints = []
        for label, ranges in constraints.items():
            if constraintToColumn[label] != None:
                continue
                
            valid = True
            for row in range(len(validTickets)):
                range1, range2 = ranges
                value = validTickets[row][column]
                if not (range1[0] <= value <= range1[1] or range2[0] <= value <= range2[1]):
                    valid = False
                    break

            if valid:
                validConstraints.append(label)
                
        if len(validConstraints) == 1:
            constraintToColumn[validConstraints[0]] = column
            

print(constraintToColumn)
res = 1
for label in constraints.keys():
    if label.startswith("departure"):
        res *= myTicket[constraintToColumn[label]]
print(res)