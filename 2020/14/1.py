mem = {}
instructions = []
mask = ""

with open("data.txt") as f:
    for line in f:
        instructions.append(line.strip().split(" = "))

for var, value in instructions:
    if var == "mask":
        mask = value
    else:
        binaryRepr = list(f"{int(value):b}".zfill(len(mask)))
        
        i = -1
        for maskingValue in mask[::-1]:
            if maskingValue != "X":
                binaryRepr[i] = maskingValue
            i -= 1

        mem[int(var.strip("mem[]"))] = int("".join(binaryRepr), 2)

print(sum(mem.values()))