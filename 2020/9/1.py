PREAMBLELENGTH = 25
numbers = []

with open("data.txt") as f:
    for line in f:
        numbers.append(int(line.strip()))

for i in range(PREAMBLELENGTH, len(numbers)):
    valid = False
    hashset = set()
    
    for j in range(i-PREAMBLELENGTH, i):
        if numbers[j] in hashset:
            valid = True
            break
        else:
            hashset.add(abs(numbers[i] - numbers[j]))

    if not valid:
        print(numbers[i])
        break