REQUIREDFIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
VALIDHCL = "abcdef0123456789"
VALIDECL = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

def validateFields(fields):
    if set(fields.keys()) != REQUIREDFIELDS:
        return False

    if not (1920 <= int(fields["byr"]) <= 2002):
        return False

    if not (2010 <= int(fields["iyr"]) <= 2020):
        return False

    if not (2020 <= int(fields["eyr"]) <= 2030):
        return False

    if fields["hgt"][-2:] not in ("in", "cm"):
        return False
    
    if fields["hgt"].endswith("cm") and not (150 <= int(fields["hgt"][:-2]) <= 193):
        return False

    if fields["hgt"].endswith("in") and not (59 <= int(fields["hgt"][:-2]) <= 76):
        return False

    if (not fields["hcl"].startswith("#")) or len(fields["hcl"]) != 7 or not all(char in VALIDHCL for char in fields["hcl"][1:]):
        return False

    if fields["ecl"] not in VALIDECL:
        return False

    if len(fields["pid"]) != 9 or not fields["pid"].isdigit():
        return False

    return True

validCount = 0
with open("data.txt") as f:
    fields = {}
    for line in f:
        if line == "\n":
            if validateFields(fields):
                validCount += 1
            fields = {}

        data = [x.split(":") for x in line.split()]
        for key, value in data:
            if key in REQUIREDFIELDS:
                fields[key] = value


    if fields == REQUIREDFIELDS:
        validCount += 1
print(validCount)