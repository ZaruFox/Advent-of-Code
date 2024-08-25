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
for ticket in otherTickets:
    for value in ticket:
        invalid = True
        for range1, range2 in constraints.values():
            if range1[0] <= value <= range1[1] or range2[0] <= value <= range2[1]:
                invalid = False
                break

        if invalid:
            res += value
print(res)

