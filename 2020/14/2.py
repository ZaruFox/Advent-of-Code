def getAllAddress(i, addressBin, mask):
    if i >= len(mask):
        return [0]
    addresses = getAllAddress(i+1, addressBin, mask)
    
    if mask[i] == "0" and addressBin[i] == "0":
        return addresses
    elif mask[i] == "X":
        return [x+2**(len(mask)-1-i) for x in addresses] + addresses
    else:
        return [x+2**(len(mask)-1-i) for x in addresses]

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
        addressBin = list(f"{int(var.strip('mem[]')) :b}".zfill(len(mask)))

        for address in getAllAddress(0, addressBin, mask):
            mem[address] = int(value)

print(sum(mem.values()))