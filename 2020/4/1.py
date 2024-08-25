REQUIREDFIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
validCount = 0

with open("data.txt") as f:
    fields = set()
    for line in f:
        if line == "\n":
            if fields == REQUIREDFIELDS:
                validCount += 1
            fields = set()

        for i in range(len(line)):
            if line[i] == ":" and line[i-3:i] in REQUIREDFIELDS:
                fields.add(line[i-3:i])


    if fields == REQUIREDFIELDS:
        validCount += 1
print(validCount)